from monogram import Monogram, validate_payload, TokenEncryptor
import requests

class Webhook(Monogram):
    @classmethod
    def set_webhook(cls, url, certificate=None, ip_address=None, max_connections=None,
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
        payload = validate_payload(locals().copy())

        # add token TokenEncryptor here.
        # if secret_token == None:
        #     TOKEN_ENCRYPTOR = TokenEncryptor()
        #     config.set('monogram', 'secret_token', TOKEN_ENCRYPTOR.encrypted_token)
        #     with open(config_path, 'w') as configfile:
        #         config.write(configfile)
        #     payload['secret_token'] = TOKEN_ENCRYPTOR.encrypted_token

        response = requests.post(cls.api_endpoint + 'setWebhook', json=payload)
        return response.json().get('ok', False)

    @classmethod
    def delete_webhook(cls, drop_pending_updates=None):
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

        response = requests.get(cls.api_endpoint + 'deleteWebhook', params=params)
        return response.json().get('ok', False)

    @classmethod
    def get_webhook_info(cls):
        """
        Retrieves the current webhook status.

        Returns:
            dict: WebhookInfo object containing the current webhook status.
        """
        response = requests.get(cls.api_endpoint + 'getWebhookInfo')
        return response.json().get('result', {})
