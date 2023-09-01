from telegram.config import API_ENDPOINT
import requests

class Webhook:
    def __init__(self):
        """
        Initializes the Webhook class.
        """
        self.base_url = API_ENDPOINT

    def set_webhook(self, url, certificate=None, ip_address=None, max_connections=None,
                    allowed_updates=None, drop_pending_updates=None, secret_token=None):
        """
        Sets the webhook URL and configures the webhook integration.

        Args:
            url (str): HTTPS URL to send updates to.
            certificate (InputFile, optional): Public key certificate for webhook certificate checks.
            ip_address (str, optional): Fixed IP address to use for sending webhook requests.
            max_connections (int, optional): Maximum allowed number of simultaneous HTTPS connections for update delivery.
            allowed_updates (list of str, optional): List of update types to receive.
            drop_pending_updates (bool, optional): Whether to drop all pending updates.
            secret_token (str, optional): Secret token to be sent in the header of webhook requests.

        Returns:
            bool: True on success, False otherwise.
        """
        payload = {'url': url}

        if certificate:
            payload['certificate'] = certificate

        if ip_address:
            payload['ip_address'] = ip_address

        if max_connections is not None:
            payload['max_connections'] = max_connections

        if allowed_updates:
            payload['allowed_updates'] = allowed_updates

        if drop_pending_updates is not None:
            payload['drop_pending_updates'] = drop_pending_updates

        headers = {}
        if secret_token:
            headers['X-Telegram-Bot-Api-Secret-Token'] = secret_token

        response = requests.post(self.base_url + 'setWebhook', json=payload, headers=headers)
        return response.json().get('ok', False)

    def delete_webhook(self, drop_pending_updates=None):
        """
        Removes the webhook integration and switches back to getUpdates.

        Args:
            drop_pending_updates (bool, optional): Whether to drop all pending updates.

        Returns:
            bool: True on success, False otherwise.
        """
        params = {}

        if drop_pending_updates is not None:
            params['drop_pending_updates'] = drop_pending_updates

        response = requests.get(self.base_url + 'deleteWebhook', params=params)
        return response.json().get('ok', False)

    def get_webhook_info(self):
        """
        Retrieves the current webhook status.

        Returns:
            dict: WebhookInfo object containing the current webhook status.
        """
        response = requests.get(self.base_url + 'getWebhookInfo')
        return response.json().get('result', {})