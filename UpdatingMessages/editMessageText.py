from typing import Optional, Dict, Any
from monogram.text import format_text
from monogram import Monogram

class edit_message(Monogram):
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

        data = {}

        if text is None:
            raise 'text are required parameters'

        data['text'] = format_text(text) # reformat text to html
        data['parse_mode'] = parse_mode

        if chat_id is not None:
            data['chat_id'] = chat_id

        if message_id is not None:
            data['message_id'] = message_id

        if message_thread_id is not None:
            data['message_thread_id'] = message_thread_id

        if inline_message_id is not None:
            data['inline_message_id'] = inline_message_id

        if entities is not None:
            data['entities'] = entities

        if disable_web_page_preview is not None:
            data['disable_web_page_preview'] = disable_web_page_preview

        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        # send post request to monogram based on method editMessageText, Construct the API endpoint URL
        cls.request('editMessageText', data)
