from typing import Optional, Dict, Any
from monogram import Monogram, validate_payload

class sendMessage(Monogram):

    def __new__(cls, chat_id: int, text: str, message_thread_id: Optional[int] = None,
                    parse_mode: Optional[str] = 'html', entities: Optional[Dict[str, Any]] = None,
                    disable_web_page_preview: Optional[bool] = None, disable_notification: Optional[bool] = None,
                    protect_content: Optional[bool] = None, reply_to_message_id: Optional[int] = None,
                    allow_sending_without_reply: Optional[bool] = None,
                    reply_markup: Optional[Dict[str, Any]] = None) -> None:

        """
        Send a text message to a chat or username of the target channel.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel
                (in the format @channel-username).
            text (str): Text of the message to be sent, 1-4096 characters after entity parsing.
            message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum;
                for forum supergroups only.
            parse_mode (str, optional): by defult is html Mode for parsing entities in the message text. See formatting options
                for more details.
            entities (Dict[str, Any], optional): A JSON-serialized list of special entities that appear in the message text,
                which can be specified instead of parse_mode.
            disable_web_page_preview (bool, optional): Disables link previews for links in this message.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
            protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
            reply_to_message_id (int, optional): If the message is a reply, ID of the original message.
            allow_sending_without_reply (bool, optional): Pass True if the message should be sent even if the specified
                replied-to message is not found.
            reply_markup (Dict[str, Any], optional): Additional interface options. A JSON-serialized object for an inline
                keyboard, custom reply keyboard, instructions to remove reply keyboard, or to force a reply from the user.

        Returns:
            None
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        cls.request(cls, method='sendMessage', data=payload)

