from monogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    InputFile,
)
from typing import Union, Optional, List, Dict
from monogram import Monogram, validate_payload


class sendAudio(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        audio: Union[str, InputFile],
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumbnail: Optional[Union[str, InputFile]] = None,
        disable_notification: Optional[bool] = False,
        protect_content: Optional[bool] = False,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = False,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> dict:
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned.
        Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

        For sending voice messages, use the sendVoice method instead.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data.
                      More information on Sending Files »
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum;
                                  for forum supergroups only (optional)
        :param caption: Audio caption, 0-1024 characters after entities parsing (optional)
        :param parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details. (optional)
        :param caption_entities: A list of special entities that appear in the caption, which can be specified instead of parse_mode (optional)
        :param duration: Duration of the audio in seconds (optional)
        :param performer: Performer (optional)
        :param title: Track name (optional)
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
                          The thumbnail should be in JPEG format and less than 200 kB in size.
                          A thumbnail's width and height should not exceed 320.
                          Ignored if the file is not uploaded using multipart/form-data.
                          Thumbnails can't be reused and can be only uploaded as a new file,
                          so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.
                          More information on Sending Files » (optional)
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound. (optional)
        :param protect_content: Protects the contents of the sent message from forwarding and saving (optional)
        :param reply_to_message_id: If the message is a reply, ID of the original message (optional)
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to
                                            message is not found (optional)
        :param reply_markup: Additional interface options. An object for an inline keyboard, custom reply keyboard,
                             instructions to remove reply keyboard, or to force a reply from the user. (optional)
        :return: A dictionary containing the response from the API call
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="sendAudio", data=payload, res=True)
        return response.json()
