from django.core.management.base import BaseCommand
from monogram import Webhook


class Command(BaseCommand):
    help = 'Sets the Telegram bot webhook'

    def add_arguments(self, parser):
        parser.add_argument('url', help='Webhook URL')
        parser.add_argument('--certificate', help='Path to the certificate file')
        parser.add_argument('--ip_address', help='Fixed IP address for webhook requests')
        parser.add_argument('--max_connections', type=int, help='Maximum allowed connections')
        parser.add_argument('--allowed_updates', nargs='+', help='Allowed update types')
        parser.add_argument('--drop_pending_updates', action='store_true', help='Drop pending updates')
        parser.add_argument('--secret_token', help='Secret token for webhook requests')

    def handle(self, *args, **options):
        url = options['url']
        certificate = options['certificate']
        ip_address = options['ip_address']
        max_connections = options['max_connections']
        allowed_updates = options['allowed_updates']
        drop_pending_updates = options['drop_pending_updates']
        secret_token = options['secret_token']
        result = Webhook.set_webhook(url=url, certificate=certificate, ip_address=ip_address,
                                     max_connections=max_connections, allowed_updates=allowed_updates,
                                     drop_pending_updates=drop_pending_updates, secret_token=secret_token)

        if result:
            self.stdout.write(self.style.SUCCESS('Webhook set successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to set webhook'))
