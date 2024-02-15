from typing import Union, List, Optional
from monogram import Monogram, validate_payload
from monogram.types import (
    MessageEntity,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Message,
)


class sendPoll(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        question: str,
        options: List[str],
        message_thread_id: Optional[int] = None,
        is_anonymous: Optional[bool] = True,
        poll_type: Optional[str] = "regular",
        allows_multiple_answers: Optional[bool] = False,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[List[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
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
        Use this method to send a native poll. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param question: Poll question, 1-300 characters
        :param options: A list of answer options, 2-10 strings 1-100 characters each
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
        :param poll_type: Poll type, "quiz" or "regular", defaults to "regular"
        :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
        :param correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode
        :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon
                            in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
        :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.
        :param explanation_entities: A list of special entities that appear in the poll explanation, which can be specified instead of parse_mode
        :param open_period: Amount of time in seconds the poll will be active after creation, 5-600.
                            Can't be used together with close_date.
        :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed.
                           Must be at least 5 and no more than 600 seconds in the future.
                           Can't be used together with open_period.
        :param is_closed: Pass True if the poll needs to be immediately closed. This can be useful for poll preview.
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
        response = cls.request(cls, method="sendPoll", data=payload, res=True)
        return response.json()
