from typing import Union, Optional
from monogram import Monogram, validate_payload
from monogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Message,
)


class sendVenue(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        message_thread_id: Optional[int] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
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
        Use this method to send information about a venue. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param latitude: Latitude of the venue
        :param longitude: Longitude of the venue
        :param title: Name of the venue
        :param address: Address of the venue
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param foursquare_id: Foursquare identifier of the venue
        :param foursquare_type: Foursquare type of the venue, if known.
                                For example, "arts_entertainment/default", "arts_entertainment/aquarium", or "food/icecream".
        :param google_place_id: Google Places identifier of the venue
        :param google_place_type: Google Places type of the venue.
                                  See supported types for more information.
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
        response = cls.request(cls, method="sendVenue", data=payload, res=True)
        return response.json()
