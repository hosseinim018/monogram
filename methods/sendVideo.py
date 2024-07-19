from typing import Union, Optional, List
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


class sendVideo(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        message_thread_id: Optional[int] = None,
        video: Union[InputFile, str] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
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
        Use this method to send video files. On success, the sent Message is returned.
        Telegram clients support MPEG4 videos (other formats may be sent as Document).
        Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a video from the Internet,
                      or upload a new video using multipart/form-data.
        :param duration: Duration of sent video in seconds
        :param width: Video width
        :param height: Video height
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
                          The thumbnail should be in JPEG format and less than 200 kB in size.
                          A thumbnail's width and height should not exceed 320.
        :param caption: Video caption (may also be used when resending videos by file_id),
                        0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption,
                                 which can be specified instead of parse_mode
        :param has_spoiler: Pass True if the video needs to be covered with a spoiler animation
        :param supports_streaming: Pass True if the uploaded video is suitable for streaming
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
        print(payload)
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="sendVideo", data=payload, res=True)
        return response.json()
