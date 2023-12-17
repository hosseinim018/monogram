from django.core.management.base import BaseCommand
from monogram import Webhook


class Command(BaseCommand):
    help = 'Deletes the Telegram bot webhook'

    def add_arguments(self, parser):
        parser.add_argument('--drop_pending_updates', action='store_true', help='Drop pending updates')

    def handle(self, *args, **options):
        drop_pending_updates = options['drop_pending_updates']
        result = Webhook.delete_webhook(drop_pending_updates=drop_pending_updates)

        if result:
            self.stdout.write(self.style.SUCCESS('Webhook deleted successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to delete webhook'))