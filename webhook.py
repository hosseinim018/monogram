import json
import logging
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import BotManager  
from .forms import BotForm
from .monoTypes import Update

logger = logging.getLogger(__name__)


class WebhookList(View):
    template_name = 'monogram/webhook_list.html' 

    def get(self, request):
        bots = BotManager.objects.all()
        form = BotForm()
        context = {
            'bots': bots,
            'form': form,
            'domain': settings.DOMAIN_NAME
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = BotForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "ربات با موفقیت افزوده شد!")
                return redirect('webhook_list')
            except Exception as e:
                messages.error(request, f"خطا در افزودن ربات: {str(e)}")
        else:
            messages.error(request, "لطفا خطاهای فرم را برطرف کنید")

        bots = BotManager.objects.all()
        context = {
            'bots': bots,
            'form': form,
            'domain': settings.DOMAIN_NAME
        }
        return render(request, self.template_name, context)


@method_decorator(csrf_exempt, name='dispatch')
class WebhookHandler(View):
    """
    Handles Telegram webhook setup, removal, and update processing
    for different bots with comprehensive error handling.
    """
    template_name = 'monogram/webhook_management.html' 
    def get(self, request, botname):
        """
        Displays webhook management interface and handles webhook setup/removal actions.
        
        Args:
            request: Django request object
            botname: Name of the bot being managed
            
        Returns:
            Rendered management page or redirect
        """
        try:
            bot = get_object_or_404(BotManager, name=botname)
            action = request.GET.get('action')
            
            # Handle webhook actions
            if action == 'set':
                if not bot.token:
                    messages.error(request, "Please set the bot token first")
                    return redirect(reverse('webhook_handler', kwargs={'botname': botname}))
                if not bot.webhook_active:
                    return self._set_webhook(request, bot)
                else:
                    messages.info(request, "Webhook already set for this bot")
                    return redirect(reverse('webhook_handler', kwargs={'botname': botname}))
            elif action == 'delete':
                return self._delete_webhook(request, bot)
            
            # Display management interface
            bots = BotManager.objects.all()
            webhook_status = self._get_webhook_info(bot) if bot.token else None
            
            context = {
                'bots': bots,
                'current_bot': bot,
                'webhook_status': webhook_status,
                'domain': settings.DOMAIN_NAME
            }
            return render(request, self.template_name, context)
            
        except Exception as e:
            logger.exception("Webhook management error")
            messages.error(request, f"System error: {str(e)}")
            return render(request, 'error.html', status=500)

    def post(self, request, botname):
        """
        Processes incoming Telegram updates via webhook.
        
        Args:
            request: Django request object
            botname: Name of the bot receiving the update
            
        Returns:
            HTTP 200 OK on success, appropriate error otherwise
        """

        try:
            bot = get_object_or_404(BotManager, name=botname)
            
            # Validate secret token
            if not self._verify_secret_token(request, bot):
                return HttpResponseForbidden("Invalid secret token")
            
            # Process update
            update_data = json.loads(request.body)
            # print(update_data)
            update = Update(bot=bot, **update_data)
            self._process_update(bot, update)
            return HttpResponse(status=200)
            
        except json.JSONDecodeError:
            logger.error("Invalid JSON payload")
            return HttpResponseBadRequest("Invalid JSON format")
        except Exception as e:
            logger.exception("Webhook processing error")
            return JsonResponse({'error': str(e)}, status=500)

    def _set_webhook(self, request, bot):
        """Configures Telegram webhook for specified bot"""
        try:
            # Build webhook URL
            webhook_path = reverse('webhook_handler', kwargs={'botname': bot.name})
            webhook_url = f"https://{settings.DOMAIN_NAME}{webhook_path}"
            # from pprint import pprint
            # pprint(vars(bot))
            # print(webhook_url)
            # Configure webhook
            params = {
                'url': webhook_url,
                'secret_token': bot.secret_token,
                'drop_pending_updates': True
            }
            response = bot.setWebhook(**params, return_response=True)
            
            if response and response.status_code == 200:
                messages.success(request, "Webhook successfully configured!")
                bot.webhook_active = True
                bot.save()
            else:
                messages.error(request, "Failed to configure webhook")
                
        except Exception as e:
            logger.exception("Webhook setup failed")
            messages.error(request, f"Webhook setup failed: {str(e)}")
        
        return self._redirect_to_management(bot.name)

    def _delete_webhook(self, request, bot):
        """Removes Telegram webhook for specified bot"""
        try:
            response = bot.deleteWebhook(return_response=True)
            
            if response and response.status_code == 200:
                messages.success(request, "Webhook successfully removed!")
                bot.webhook_active = False
                bot.save()
            else:
                messages.error(request, "Failed to remove webhook")
                
        except Exception as e:
            logger.exception("Webhook removal failed")
            messages.error(request, f"Webhook removal failed: {str(e)}")
        
        return self._redirect_to_management(bot.name)

    def _get_webhook_info(self, bot):
        """Retrieves current webhook information (for UI display)"""
        try:
            response = bot.getWebhookInfo(return_response=True)
            return response.json() if response else None
            
        except Exception:
            logger.exception("Failed to get webhook info")
            return None

    def _verify_secret_token(self, request, bot):
        """Validates X-Telegram-Bot-Api-Secret-Token header"""
        if not bot.secret_token:
            return True
            
        incoming_token = request.headers.get('X-Telegram-Bot-Api-Secret-Token', '')
        return incoming_token == bot.secret_token

    def _redirect_to_management(self, botname):
        """Safe redirect to management page"""
        return redirect(reverse('webhook_handler', kwargs={'botname': botname}))
      
    def _process_update(self, bot, update):
        """Processes incoming Telegram update (to be implemented)"""
        logger.info(f"Received update for {bot.name}: {update}")
        
        if not bot.object:
            logger.error(f"No bot class defined for {bot.name}")
            return
            
        try:
            # load dynamic bot class
            module_path, class_name = bot.object.rsplit('.', 1)
            module = __import__(module_path, fromlist=[class_name])
            BotClass = getattr(module, class_name)
           
            # create instance from bot class and process update
            bot_instance = BotClass(bot, update)
            
            # bot_instance.handle_update()
            
        except ImportError as e:
            logger.exception(f"Failed to import bot class: {bot.object}")
        except AttributeError:
            logger.exception(f"Class not found: {bot.object}")
        except Exception as e:
            logger.exception(f"Error processing update: {str(e)}")