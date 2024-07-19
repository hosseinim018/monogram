from typing import Optional, Dict, Any
from monogram.text import format_text
from monogram import Monogram, validate_payload

class editMessageText(Monogram):
    def __new__(cls, text: str, chat_id: Optional[int]= None, message_id: Optional[int] = None, message_thread_id: Optional[int] = None, inline_message_id: Optional[str] = None,
                     parse_mode: Optional[str] = 'html', entities: Optional[Dict[str, Any]] = None,
                     disable_web_page_preview: Optional[bool] = None, reply_markup: Optional[Dict[str, Any]] = None) -> None:
        """
        Edit a text or game message.

        On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Parameters:
            chat_id (int): Unique identifier for the target chat or username of the target channel
                (in the format @channelusername). Required if inline_message_id is not specified.
            text (str): New text of the message, 1-4096 characters after entities parsing. Required.
            message_id (int, optional): Required if inline_message_id is not specified. Identifier of the message to edit
            message_thread_id (int, optional): Identifier of the message thread.
            inline_message_id (str, optional): Identifier of the inline message.
            parse_mode (str): by defult is html, Mode for parsing entities in the message text. See formatting options for more details.
            entities (List[MessageEntity], optional): A list of special entities that appear in the message text,
                which can be specified instead of parse_mode.
            disable_web_page_preview (bool, optional): Disables link previews for links in this message.
            reply_markup (Dict[str, Any], optional): An object for an inline keyboard.

        Returns:
            None
        """
        payload = validate_payload(locals().copy())
        # send post request to monogram based on method editMessageText, Construct the API endpoint URL
        cls.request(cls, method='editMessageText', data=payload)