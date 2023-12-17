from typing import Union, Optional
from monogram import Monogram, validate_payload

class sendChatAction(Monogram):
    def __new__(cls, chat_id: Union[int, str], action: str, message_thread_id: Optional[int] = None) -> bool:
        """
        Use this method when you need to tell the user that something is happening on the bot's side.
        The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).
        Returns True on success.

        Example: The ImageBot needs some time to process a request and upload the image.
        Instead of sending a text message along the lines of “Retrieving image, please wait…”,
        the bot may use sendChatAction with action = upload_photo.
        The user will see a “sending photo” status for the bot.

        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive:
                       "typing" for text messages, "upload_photo" for photos, "record_video" or "upload_video" for videos,
                       "record_voice" or "upload_voice" for voice notes, "upload_document" for general files,
                       "choose_sticker" for stickers, "find_location" for location data,
                       "record_video_note" or "upload_video_note" for video notes.
        :param message_thread_id: Unique identifier for the target message thread; supergroups only
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='sendChatAction', data=payload, res=True)
        return response.json()