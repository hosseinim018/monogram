from django.core.management.base import BaseCommand, CommandError
from monogram.models import BotManager
from django.conf import settings
import sys

class Command(BaseCommand):
    help = 'Manage Telegram bots through command line interface'

    def add_arguments(self, parser):
        parser.add_argument('action', nargs='?', type=str, help='Action to perform: add, list, delete or [information/setWebhook/deleteWebhook/webhookInfo] botname')
        parser.add_argument('botname', nargs='?', type=str, help='Name of the bot to manage')

    def handle(self, *args, **options):
        action = options.get('action')
        botname = options.get('botname')

        if not action:
            self.stdout.write(self.style.ERROR('Please provide an action'))
            return

        if action == 'list':
            self.list_bots()
        elif action == 'add':
            self.add_bot()
        elif action == 'delete':
            if not botname:
                self.stdout.write(self.style.ERROR('Please provide a bot name to delete'))
                return
            self.delete_bot(botname)
        elif action in ['information', 'setWebhook', 'deleteWebhook', 'webhookInfo']:
            if not botname:
                self.stdout.write(self.style.ERROR(f'Please provide a bot name for {action}'))
                return
            self.manage_bot(action, botname)
        else:
            self.stdout.write(self.style.ERROR('Invalid action'))

    def list_bots(self):
        """Display list of bots and handle interactive mode"""
        bots = BotManager.objects.all()
        
        if not bots.exists():
            self.stdout.write(self.style.WARNING('No bots have been added yet.'))
            return

        # Display bot list
        self.stdout.write('\nAvailable bots:')
        for i, bot in enumerate(bots, 1):
            self.stdout.write(f'[{i}] {bot.name}')

        # Interactive mode
        self.stdout.write('\nEnter bot number to see options (or "c" to cancel): ')
        try:
            choice = input().strip()
            
            if choice.lower() == 'c':
                return
                
            try:
                bot_index = int(choice)
                if 1 <= bot_index <= len(bots):
                    bot = bots[bot_index - 1]
                    self.show_bot_options(bot)
                else:
                    self.stdout.write(self.style.ERROR('Invalid bot number'))
                    return
                    
            except ValueError:
                self.stdout.write(self.style.ERROR('Please enter a valid number'))
                
        except KeyboardInterrupt:
            self.stdout.write('\nOperation cancelled by user')
            
    def show_bot_options(self, bot):
        """Show options for a specific bot"""
        options = [
            'show information',
            'set webhook',
            'delete webhook',
            'webhook info',
            'edit bot',
            'delete bot'
        ]
        
        self.stdout.write('\nAvailable options:')
        for i, option in enumerate(options, 1):
            self.stdout.write(f'[{i}] {option}')
        self.stdout.write('enter "c" to cancel')
        
        try:
            choice = input('\nEnter option number: ').strip()
            
            if choice.lower() == 'c':
                return
                
            try:
                option = int(choice)
                if option < 1 or option > len(options):
                    self.stdout.write(self.style.ERROR('Invalid option number'))
                    return
                    
                if option == 1:
                    self.show_bot_information(bot)
                elif option == 2:
                    self.set_webhook(bot)
                elif option == 3:
                    self.delete_webhook(bot)
                elif option == 4:
                    self.show_webhook_info(bot)
                elif option == 5:
                    self.edit_bot(bot)
                elif option == 6:
                    self._confirm_and_delete_bot(bot)
                    
            except ValueError:
                self.stdout.write(self.style.ERROR('Please enter a valid number'))
                
        except KeyboardInterrupt:
            self.stdout.write('\nOperation cancelled by user')

    def show_bot_information(self, bot):
        """Display detailed bot information"""
        info = [
            ('Name', bot.name),
            ('Owner', bot.owner),
            ('Secret Token', bot.secret_token),
            ('Endpoint', bot.api_endpoint),
            ('Proxy', bot.proxy),
            ('Proxy URL', bot.proxy_url),
            ('Webhook Active', bot.webhook_active),
            ('Created At', bot.created_at),
            ('Updated At', bot.updated_at),
            ('Object', bot.object),
        ]
        
        self.stdout.write('\nBot Information:')
        for key, value in info:
            self.stdout.write(f'{key}: {value}')

    def set_webhook(self, bot):
        """Set webhook for the bot"""
        if not bot.token:
            self.stdout.write(self.style.ERROR('Bot token is not set'))
            return
            
        webhook_path = f'/monogram/webhook/{bot.name}/'
        webhook_url = f'https://{settings.DOMAIN_NAME}{webhook_path}'
        
        try:
            params = {
                'url': webhook_url,
                'secret_token': bot.secret_token,
                'drop_pending_updates': True
            }
            response = bot.setWebhook(**params, return_response=True)
            
            # response = bot.setWebhook(
            #     url=webhook_url,
            #     secret_token=bot.secret_token,
            #     drop_pending_updates=True,
            #     return_response=True
            # )
            
            if response:
                bot.webhook_active = True
                bot.save()
                self.stdout.write(self.style.SUCCESS('Webhook successfully configured!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to configure webhook'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Webhook setup failed: {str(e)}'))

    def delete_webhook(self, bot):
        """Delete webhook for the bot"""
        try:
            response = bot.deleteWebhook(return_response=True)
            
            if response:
                bot.webhook_active = False
                bot.save()
                self.stdout.write(self.style.SUCCESS('Webhook successfully removed!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to remove webhook'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Webhook removal failed: {str(e)}'))

    def show_webhook_info(self, bot):
        """Show webhook information for the bot"""
        try:
            response = bot.getWebhookInfo(return_response=True)
            if response:
                info = response
                self.stdout.write('\nWebhook Information:')
                for key, value in info.items():
                    self.stdout.write(f'{key}: {value}')
            else:
                self.stdout.write(self.style.ERROR('Failed to get webhook information'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to get webhook info: {str(e)}'))

    def manage_bot(self, action, botname):
        """Handle direct bot management actions"""
        try:
            bot = BotManager.objects.get(name=botname)
            
            if action == 'information':
                self.show_bot_information(bot)
            elif action == 'setWebhook':
                self.set_webhook(bot)
            elif action == 'deleteWebhook':
                self.delete_webhook(bot)
            elif action == 'webhookInfo':
                self.show_webhook_info(bot)
                
        except BotManager.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Bot with name "{botname}" does not exist'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))

    def add_bot(self):
        """Interactive bot creation process"""
        self.stdout.write(self.style.NOTICE("""
Welcome to the Telegram Bot Creation Process!
This wizard will guide you through adding a new bot to the system.
You will need to provide:
- Bot name (for system identification)
- Bot username (e.g, @monogram)
- Owner ID (Telegram user ID of the bot owner)
- Bot token (from @BotFather)
- Secret token (optional, for webhook security)
- Bot class path (e.g., Bots.bot.bot1)
- Proxy settings (optional)
        """))
        
        self.stdout.write("\nPress 'y' to continue or 'c' to cancel: ")
        choice = input().strip().lower()
        
        if choice != 'y':
            self.stdout.write(self.style.NOTICE("Operation cancelled."))
            return
            
        bot_data = {}
        try:
            # Get bot information
            bot_data = self._collect_bot_data()
            
            while True:
                # Show summary and get confirmation
                self._show_bot_data_summary(bot_data)
                self.stdout.write("\nDo you want to:\n[s] Save the bot\n[e] Edit information\n[c] Cancel\nYour choice: ")
                
                choice = input().strip().lower()
                
                if choice == 's':
                    self._save_bot(bot_data)
                    break
                elif choice == 'e':
                    bot_data = self._edit_bot_data(bot_data)
                elif choice == 'c':
                    self.stdout.write(self.style.NOTICE("Operation cancelled."))
                    break
                else:
                    self.stdout.write(self.style.ERROR("Invalid choice. Please try again."))
                    
        except KeyboardInterrupt:
            self.stdout.write("\nOperation cancelled by user.")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"\nError: {str(e)}"))

    def _collect_bot_data(self):
        """Collect bot information interactively"""
        bot_data = {}
        
        # Get name
        while True:
            self.stdout.write("\nEnter bot name (for system identification): ")
            name = input().strip()
            if name:
                if not BotManager.objects.filter(name=name).exists():
                    bot_data['name'] = name
                    break
                else:
                    self.stdout.write(self.style.ERROR("This bot name already exists. Please choose another name."))
            else:
                self.stdout.write(self.style.ERROR("Bot name cannot be empty."))
        
        # Get username
        while True:
            self.stdout.write("\nEnter bot username (e.g, @monogram): ")
            username = input().strip()
            if name:
                if not BotManager.objects.filter(username=username).exists():
                    bot_data['username'] = username
                    break
                else:
                    self.stdout.write(self.style.ERROR("This bot username already exists. Please choose another username."))
            else:
                self.stdout.write(self.style.ERROR("Bot username cannot be empty."))
        
        # Get owner ID
        while True:
            self.stdout.write("\nEnter owner's Telegram user ID (numeric): ")
            owner = input().strip()
            if owner.isdigit():
                bot_data['owner'] = int(owner)
                break
            else:
                self.stdout.write(self.style.ERROR("Owner ID must be a number."))
        
        # Get token
        while True:
            self.stdout.write("\nEnter bot token (from @BotFather): ")
            token = input().strip()
            if token:
                bot_data['token'] = token
                break
            else:
                self.stdout.write(self.style.ERROR("Bot token cannot be empty."))
        
        # Get secret token
        self.stdout.write("\nEnter secret token (press Enter to generate automatically): ")
        secret_token = input().strip()
        bot_data['secret_token'] = secret_token if secret_token else None
        
        # Get bot class path
        while True:
            self.stdout.write("\nEnter bot class path (e.g., Bots.bot.bot1): ")
            object_path = input().strip()
            if object_path:
                bot_data['object'] = object_path
                break
            else:
                self.stdout.write(self.style.ERROR("Bot class path cannot be empty."))
        
        # Get proxy settings
        self.stdout.write("\nDo you want to use a proxy? (y/n): ")
        use_proxy = input().strip().lower() == 'y'
        bot_data['proxy'] = use_proxy
        
        if use_proxy:
            while True:
                self.stdout.write("\nEnter proxy URL (e.g., http://proxy.example.com:8080): ")
                proxy_url = input().strip()
                if proxy_url:
                    bot_data['proxy_url'] = proxy_url
                    break
                else:
                    self.stdout.write(self.style.ERROR("Proxy URL cannot be empty when proxy is enabled."))
        else:
            bot_data['proxy_url'] = None
            
        return bot_data

    def _show_bot_data_summary(self, bot_data):
        """Display bot data summary"""
        self.stdout.write("\nBot Information Summary:")
        self.stdout.write("-" * 40)
        
        fields = [
            ('Name', 'name'),
            ('Username', 'username'),
            ('Owner ID', 'owner'),
            ('Token', 'token'),
            ('Secret Token', 'secret_token', '(Will be generated automatically)'),
            ('Bot Class Path', 'object'),
            ('Use Proxy', 'proxy'),
            ('Proxy URL', 'proxy_url'),
        ]
        
        for i, field_info in enumerate(fields):
            field_name = field_info[0]
            field_key = field_info[1]
            default_msg = field_info[2] if len(field_info) > 2 else None
            
            value = bot_data.get(field_key)
            if value is None and default_msg:
                value = default_msg
            
            self.stdout.write(f"[{i}] {field_name}: {value}")

    def _edit_bot_data(self, bot_data):
        """Edit bot data interactively"""
        while True:
            self._show_bot_data_summary(bot_data)
            self.stdout.write("\nEnter the number of the field to edit (or 'c' to finish editing): ")
            
            choice = input().strip().lower()
            if choice == 'c':
                break
                
            try:
                field_num = int(choice)
                fields = [
                    ('name', "Enter new bot name: ", self._validate_name),
                    ('username', "Enter new bot username: ", self._validate_username),
                    ('owner', "Enter new owner ID: ", self._validate_owner),
                    ('token', "Enter new bot token: ", self._validate_token),
                    ('secret_token', "Enter new secret token (Enter for automatic): ", self._validate_secret_token),
                    ('object', "Enter new bot class path: ", self._validate_object),
                    ('proxy', "Use proxy? (y/n): ", self._validate_proxy),
                    ('proxy_url', "Enter new proxy URL: ", self._validate_proxy_url),
                ]
                
                if 0 <= field_num < len(fields):
                    field_key, prompt, validator = fields[field_num]
                    
                    # Special handling for proxy
                    if field_key == 'proxy':
                        bot_data['proxy'] = input(prompt).strip().lower() == 'y'
                        if bot_data['proxy']:
                            bot_data['proxy_url'] = self._validate_proxy_url(input("Enter proxy URL: "))
                        else:
                            bot_data['proxy_url'] = None
                    else:
                        value = input(prompt).strip()
                        bot_data[field_key] = validator(value) if value else None
                else:
                    self.stdout.write(self.style.ERROR("Invalid field number."))
                    
            except ValueError:
                self.stdout.write(self.style.ERROR("Please enter a valid number."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))
                
        return bot_data

    def _save_bot(self, bot_data):
        """Save bot to database"""
        try:
            bot = BotManager(**bot_data)
            bot.full_clean()
            bot.save()
            self.stdout.write(self.style.SUCCESS(f"\nBot '{bot.name}' successfully created!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"\nFailed to create bot: {str(e)}"))

    def _validate_name(self, value, bot_instance=None):
        """Validate bot name"""
        if not value:
            raise ValueError("Bot name cannot be empty")
        query = BotManager.objects.filter(name=value)
        if bot_instance:
            query = query.exclude(pk=bot_instance.pk)
        if query.exists():
            raise ValueError("This bot name already exists")
        return value

    def _validate_username(self, value, bot_instance=None):
        """Validate bot username"""
        if not value:
            raise ValueError("Bot username cannot be empty")
        query = BotManager.objects.filter(username=value)
        if bot_instance:
            query = query.exclude(pk=bot_instance.pk)
        if query.exists():
            raise ValueError("This bot username already exists")
        return value

    def _validate_owner(self, value, bot_instance=None):
        """Validate owner ID"""
        if not value.isdigit():
            raise ValueError("Owner ID must be a number")
        return int(value)

    def _validate_token(self, value, bot_instance=None):
        """Validate bot token"""
        if not value:
            raise ValueError("Bot token cannot be empty")
        return value

    def _validate_secret_token(self, value, bot_instance=None):
        """Validate secret token"""
        return value if value else None

    def _validate_object(self, value, bot_instance=None):
        """Validate bot class path"""
        if not value:
            raise ValueError("Bot class path cannot be empty")
        return value

    def _validate_proxy(self, value, bot_instance=None):
        """Validate proxy setting"""
        return value.lower() == 'y'

    def _validate_proxy_url(self, value, bot_instance=None):
        """Validate proxy URL"""
        # This validation is only for direct input, proxy URL can be empty if proxy is false
        if value:
            return value
        return None

    def delete_bot(self, botname):
        """Delete a bot by name with confirmation"""
        try:
            bot = BotManager.objects.get(name=botname)
            self._confirm_and_delete_bot(bot)
        except BotManager.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Bot with name "{botname}" does not exist'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error deleting bot: {str(e)}'))

    def _confirm_and_delete_bot(self, bot):
        """Ask for confirmation and delete the bot"""
        self.stdout.write(self.style.WARNING(f'\nYou are about to delete the bot "{bot.name}"'))
        self.stdout.write(self.style.WARNING('This action cannot be undone!'))
        self.stdout.write("\nEnter 'yes' to confirm deletion or anything else to cancel: ")
        
        try:
            confirmation = input().strip().lower()
            
            if confirmation == 'yes':
                # If webhook is active, try to delete it first
                if bot.webhook_active:
                    try:
                        response = bot.deleteWebhook(return_response=True)
                        if response and response.status_code == 200:
                            self.stdout.write(self.style.SUCCESS('Webhook removed successfully'))
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Failed to remove webhook: {str(e)}'))
                
                # Delete the bot
                bot.delete()
                self.stdout.write(self.style.SUCCESS(f'Bot "{bot.name}" has been deleted successfully'))
            else:
                self.stdout.write(self.style.NOTICE('Deletion cancelled'))
        except KeyboardInterrupt:
            self.stdout.write('\nOperation cancelled by user')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during deletion: {str(e)}'))

    def edit_bot(self, bot):
        """Interactive bot editing process"""
        self.stdout.write(self.style.NOTICE(f"\nEditing bot: {bot.name}"))
        
        while True:
            fields = [
                ('Name', 'name', bot.name, self._validate_name),
                ('Username', 'username', bot.username, self._validate_username),
                ('Owner', 'owner', bot.owner, self._validate_owner),
                ('Token', 'token', bot.token, self._validate_token),
                ('Secret Token', 'secret_token', bot.secret_token, self._validate_secret_token),
                ('Bot Class Path', 'object', bot.object, self._validate_object),
                ('Proxy', 'proxy', bot.proxy, self._validate_proxy),
                ('Proxy URL', 'proxy_url', bot.proxy_url, self._validate_proxy_url),
            ]

            self.stdout.write("\nSelect a field to edit:")
            for i, (label, _, value, _) in enumerate(fields, 1):
                self.stdout.write(f"[{i}] {label}: {value}")
            
            self.stdout.write("\nEnter field number, 's' to save and exit, or 'c' to cancel: ")
            choice = input().strip().lower()

            if choice == 'c':
                self.stdout.write(self.style.NOTICE("Editing cancelled."))
                return
            if choice == 's':
                try:
                    bot.full_clean()
                    bot.save()
                    self.stdout.write(self.style.SUCCESS(f"Bot '{bot.name}' updated successfully!"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to save bot: {e}"))
                return

            try:
                field_num = int(choice)
                if 1 <= field_num <= len(fields):
                    label, key, _, validator = fields[field_num - 1]
                    
                    prompt = f"Enter new {label}: "
                    if key == 'proxy':
                        prompt = "Use proxy? (y/n): "
                    
                    new_value_str = input(prompt).strip()

                    try:
                        # For proxy, the validator returns a boolean directly
                        if key == 'proxy':
                            new_value = validator(new_value_str)
                            setattr(bot, key, new_value)
                            if not new_value: # If proxy is disabled, clear proxy_url
                                setattr(bot, 'proxy_url', None)
                        # For other fields, validator returns the cleaned value
                        else:
                            # Pass bot instance to validator for context
                            new_value = validator(new_value_str, bot_instance=bot)
                            setattr(bot, key, new_value)
                        
                        self.stdout.write(self.style.SUCCESS(f"{label} updated."))

                    except ValueError as e:
                        self.stdout.write(self.style.ERROR(str(e)))

                else:
                    self.stdout.write(self.style.ERROR("Invalid field number."))
            except ValueError:
                self.stdout.write(self.style.ERROR("Please enter a valid number, 's', or 'c'."))
            except KeyboardInterrupt:
                self.stdout.write("\nOperation cancelled by user.")
                return
