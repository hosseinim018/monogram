from typing import Union, Optional
from monogram import Monogram, validate_payload
from monogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Message,
)


class sendLocation(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        message_thread_id: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
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
        Use this method to send a point on the map. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param latitude: Latitude of the location
        :param longitude: Longitude of the location
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
        :param live_period: Period in seconds for which the location will be updated.
                            Should be between 60 and 86400. (see Live Locations)
        :param heading: For live locations, a direction in which the user is moving, in degrees.
                        Must be between 1 and 360 if specified.
        :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters.
                                       Must be between 1 and 100000 if specified.
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
        response = cls.request(cls, method="sendLocation", data=payload, res=True)
        return response.json()
