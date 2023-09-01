from django.core.management.base import BaseCommand
from telegram.bot.connection.Webhook import Webhook

class Command(BaseCommand):
    help = 'Retrieves the current Telegram bot webhook information'

    def handle(self, *args, **options):
        webhook = Webhook()
        webhook_info = webhook.get_webhook_info()

        self.stdout.write(self.style.SUCCESS('Webhook information retrieved successfully:'))
        self.stdout.write(str(webhook_info))