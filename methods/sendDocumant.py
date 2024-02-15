from typing import Union, Optional, List
from monogram import Monogram, validate_payload
from monogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    InputFile,
    MessageEntity,
    Message,
)


class sendDocumant(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        message_thread_id: Optional[int] = None,
        document: Union[InputFile, str] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send general files. On success, the sent Message is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended),
                         pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
                          The thumbnail should be in JPEG format and less than 200 kB in size.
                          A thumbnail's width and height should not exceed 320.
        :param caption: Document caption (may also be used when resending documents by file_id),
                        0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption,
                                 which can be specified instead of parse_mode
        :param disable_content_type_detection: Disables automatic server-side content type detection
                                               for files uploaded using multipart/form-data
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Additional interface options.
                             A JSON-serialized object for an inline keyboard, custom reply keyboard,
                             instructions to remove reply keyboard or to force a reply from the user.
        :return: The sent Message object
        """
        # Your implementation here
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="sendDocumant", data=payload, res=True)
        return response.json()
