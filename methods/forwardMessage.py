from typing import Union
from monogram import Monogram, validate_payload
class forwardMessage(Monogram):
    def __new__(cls, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int,
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
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='forwardMessage', data=payload, res=True)
        return response.json()


