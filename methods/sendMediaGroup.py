from typing import Union, Optional, List
from monogram import Monogram, validate_payload
from monogram.types import (
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)


class sendMediaGroup(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        media: List[
            Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]
        ],
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> List[Message]:
        """
        Use this method to send a group of photos, videos, documents or audios as an album.
        On success, an array of Messages that were sent is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items.
                      Each item in the array can be an instance of InputMediaAudio, InputMediaDocument, InputMediaPhoto, or InputMediaVideo.
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_notification: Sends messages silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent messages from forwarding and saving
        :param reply_to_message_id: If the messages are a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :return: An array of sent Message objects
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="sendMediaGroup", data=payload, res=True)
        return response.json()
