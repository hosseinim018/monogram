from typing import Union, Optional
from monogram import Monogram, validate_payload
from monogram.types import (
    InputFile,
    MessageEntity,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Message,
)


class sendVideoNote(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        message_thread_id: Optional[int] = None,
        video_note: Union[InputFile, str] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
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
        Use this method to send video messages. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended)
                           or upload a new video using multipart/form-data.
        :param duration: Duration of sent video in seconds
        :param length: Video width and height, i.e. diameter of the video message
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
                          The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
                          Ignored if the file is not uploaded using multipart/form-data.
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Additional interface options.
                             A JSON-serialized object for an inline keyboard, custom reply keyboard,
                             instructions to remove reply keyboard or to force a reply from the user.
        :return: The sent Message object
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="sendVideoNote", data=payload, res=True)
        return response.json()
