import requests
from typing import Union

def forward_message(chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int,
                    message_thread_id: Union[int, None] = None, disable_notification: bool = False,
                    protect_content: bool = False) -> dict:
    """
    Use this method to forward messages of any kind.
    Service messages can't be forwarded.
    On success, the sent Message is returned.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param from_chat_id: Unique identifier for the chat where the original message was sent
                        (or channel username in the format @channelusername)
    :param message_id: Message identifier in the chat specified in from_chat_id
    :param message_thread_id: Unique identifier for the target message thread (topic) of the forum;
                              for forum supergroups only (optional)
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound. (optional)
    :param protect_content: Protects the contents of the forwarded message from forwarding and saving (optional)
    :return: A dictionary containing the response from the API call
    """
    # Replace 'YOUR_TOKEN' with your actual bot token
    token = 'YOUR_TOKEN'
    base_url = f'https://api.telegram.org/bot{token}/'
    method = 'forwardMessage'

    params = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'message_thread_id': message_thread_id,
        'disable_notification': disable_notification,
        'protect_content': protect_content
    }

    url = base_url + method
    response = requests.get(url, params=params)
    return response.json()


