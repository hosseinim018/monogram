from django.db import models
from django.core.exceptions import ValidationError
from monogram.methods import Methods
import logging
import secrets


logger = logging.getLogger(__name__)

class BotManager(Methods, models.Model):
    """Telegram Bot model with direct API method access"""
    name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    owner = models.BigIntegerField(blank=True, null=True, help_text="Owner's Telegram user ID")
    token = models.CharField(max_length=100)
    secret_token = models.CharField(max_length=100, blank=True, null=True)
    endpoint = models.CharField(
        max_length=100, 
        default='api.telegram.org',
        help_text="Telegram API endpoint (e.g., 'api.telegram.org')"
    )
    proxy = models.BooleanField(default=False)
    proxy_url = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        help_text="Proxy URL (e.g., 'http://proxy.example.com:8080')"
    )
    webhook_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="path of bot class(e.g., Bots.bot.bot1)"
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize both the Django model and the Methods API client
        
        Note: We need to initialize models.Model first to ensure fields are set
        before initializing the Methods class
        """
        # Initialize Django model first
        models.Model.__init__(self, *args, **kwargs)
        
        # Initialize Methods with current credentials
        Methods.__init__(
            self,
            token=self.token,
            secret_token=self.secret_token,
            endpoint=self.endpoint,
            proxy=self.proxy,
            proxy_url=self.proxy_url,
        )

    class Meta:
        verbose_name = "Telegram Bot"
        verbose_name_plural = "Telegram Bots"

    def __str__(self):
        return f"{self.name} ({'Active' if self.webhook_active else 'Inactive'})"

    # def __getattr__(self, name):
    #     """
    #     Delegate unknown methods to the Methods API client
    #     Allows direct calls like bot.sendMessage(...)
    #     """
    #     # Only delegate if the attribute exists in Methods
    #     if hasattr(Methods, name):
    #         return getattr(self, name)
    #     raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def clean(self):
        """Validate bot configuration"""
        errors = {}
        
        # Token format validation
        # if not self.token.startswith('bot'):
        #     errors['token'] = "Bot token should start with 'bot'"
        
        # Proxy configuration
        if self.proxy and not self.proxy_url:
            errors['proxy_url'] = "Proxy URL is required when proxy is enabled"
            
        # Test API connection only when token is changed and bot exists in DB
        if not errors and self.pk:
            try:
                orig = BotManager.objects.get(pk=self.pk)
                if orig.token != self.token:
                    # Reinitialize with new token for validation
                    Methods.__init__(
                        self,
                        token=self.token,
                        secret_token=self.secret_token,
                        endpoint=self.endpoint,
                        proxy=self.proxy,
                        proxy_url=self.proxy_url,
                    )
                    
                    # Test API connection
                    me = self.get_me()
                    if not me or not me.get('ok'):
                        errors['token'] = "Failed to verify token with Telegram API"
            except BotManager.DoesNotExist:
                pass  # New instance, no need to validate against DB
            except Exception as e:
                errors['token'] = f"API connection failed: {str(e)}"
        
        if errors:
            raise ValidationError(errors)
    
    def save(self, *args, **kwargs):
        """Save the model and reinitialize API client with current credentials"""
        # Run full validation first
        self.full_clean()
        if not self.secret_token:
            self.secret_token = secrets.token_urlsafe(32)
        
        # Save the model
        super().save(*args, **kwargs)
        
        # Reinitialize API client with current credentials
        Methods.__init__(
            self,
            token=self.token,
            secret_token=self.secret_token,
            endpoint=self.endpoint,
            proxy=self.proxy,
            proxy_url=self.proxy_url,
        )
