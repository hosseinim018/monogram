import requests
from typing import Union, Optional, List, Dict

def send_photo(chat_id: Union[int, str], photo: Union[str, InputFile],
               message_thread_id: Optional[int] = None, caption: Optional[str] = None,
               parse_mode: Optional[str] = None, caption_entities: Optional[List[Dict]] = None,
               has_spoiler: Optional[bool] = False, disable_notification: Optional[bool] = False,
               protect_content: Optional[bool] = False, reply_to_message_id: Optional[int] = None,
               allow_sending_without_reply: Optional[bool] = False,
               reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None) -> dict:
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
    # Replace 'YOUR_TOKEN' with your actual bot token
    token = 'YOUR_TOKEN'
    base_url = f'https://api.telegram.org/bot{token}/'
    method = 'sendPhoto'

    params = {
        'chat_id': chat_id,
        'photo': photo,
        'message_thread_id': message_thread_id,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'has_spoiler': has_spoiler,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'reply_to_message_id': reply_to_message_id,
        'allow_sending_without_reply': allow_sending_without_reply,
        'reply_markup': reply_markup
    }

    url = base_url + method
    response = requests.get(url, params=params)
    return response.json()