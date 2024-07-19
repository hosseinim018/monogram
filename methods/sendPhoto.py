from monogram import Monogram, validate_payload
from typing import Union, Optional, List, Dict
from monogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    InputFile,
    Message
)


class sendPhoto(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        photo: Union[str, InputFile],
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        has_spoiler: Optional[bool] = False,
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
    ) -> Message:
        """
        Use this method to send photos.
        On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo
                      using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must
                      not exceed 10000 in total. Width and height ratio must be at most 20. More information on Sending Files »
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum;
                                  for forum supergroups only (optional)
        :param caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing (optional)
        :param parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details. (optional)
        :param caption_entities: A list of special entities that appear in the caption, which can be specified instead of parse_mode (optional)
        :param has_spoiler: Pass True if the photo needs to be covered with a spoiler animation (optional)
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound. (optional)
        :param protect_content: Protects the contents of the sent message from forwarding and saving (optional)
        :param reply_to_message_id: If the message is a reply, ID of the original message (optional)
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to
                                            message is not found (optional)
        :param reply_markup: Additional interface options. An object for an inline keyboard, custom reply keyboard,
                             instructions to remove reply keyboard, or to force a reply from the user. (optional)
        :return: A dictionary containing the response from the API call
        """
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        _locals = locals().copy()

        if isinstance(photo, InputFile):
            # print("photo is an InputFile object")
            _locals.pop('photo')
            payload = validate_payload(_locals)
            file = open(photo.file_path, 'rb')
            file = {"photo": file}

            response = cls.request(cls, method="sendPhoto", data=payload, files=file, res=True)

        else:
            # print("photo is a string")
            payload = validate_payload(_locals)
            response = cls.request(cls, method="sendPhoto", data=payload, res=True)

        response = response.json()
        print(response)
        result = response['result']
        if result:
            result["from_user"] = result.pop("from")


        return Message(**result)
