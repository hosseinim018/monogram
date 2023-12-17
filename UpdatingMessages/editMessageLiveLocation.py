from typing import Optional, Union

def edit_message_live_location(
    latitude: float,
    longitude: float,
    chat_id: Optional[Union[int, str]] = None,
    message_id: Optional[int] = None,
    inline_message_id: Optional[str] = None,
    horizontal_accuracy: Optional[float] = None,
    heading: Optional[int] = None,
    proximity_alert_radius: Optional[int] = None,
    reply_markup: Optional[dict] = None,
) -> Union[bool, dict]:
    """
    Use this method to edit live location messages.
    A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation.
    On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    :param chat_id: Required if inline_message_id is not specified.
                    Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified.
                       Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified.
                              Identifier of the inline message
    :param latitude: Latitude of the new location
    :param longitude: Longitude of the new location
    :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    :param heading: Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :param proximity_alert_radius: The maximum distance for proximity alerts about approaching another chat member, in meters.
                                   Must be between 1 and 100000 if specified.
    :param reply_markup: A JSON-serialized object for a new inline keyboard.
    :return: If the edited message is not an inline message, the edited Message is returned,
             otherwise True is returned.
    """
    # Your implementation here
    pass