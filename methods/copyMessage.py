from typing import Union, Optional, List, Dict
from monogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
from monogram import Monogram, validate_payload


class copyMessage(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        disable_notification: Optional[bool] = False,
        protect_content: Optional[bool] = False,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = False,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None,
    ) -> dict:
        """
        Use this method to copy messages of any kind.
        Service messages and invoice messages can't be copied.
        A quiz poll can be copied only if the value of the field correct_option_id is known to the bot.
        The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message.
        Returns the MessageId of the sent message on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message was sent
                            (or channel username in the format @channelusername)
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum;
                                  for forum supergroups only (optional)
        :param caption: New caption for media, 0-1024 characters after entities parsing. If not specified,
                        the original caption is kept (optional)
        :param parse_mode: Mode for parsing entities in the new caption. See formatting options for more details. (optional)
        :param caption_entities: A list of special entities that appear in the new caption, which can be specified
                                 instead of parse_mode (optional)
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
        response = cls.request(cls, method="copyMessage", data=payload, res=True)
        return response.json()
