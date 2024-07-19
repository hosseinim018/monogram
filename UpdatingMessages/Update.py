from typing import Optional
from ..types import *
from dataclasses import dataclass


class InlineQuery:
    pass


class ChosenInlineResult:
    pass


class ShippingQuery:
    pass


class PreCheckoutQuery:
    pass


@dataclass
class Update:
    def __init__(
        self,
        update_id: int,
        message: Optional[dict] = None,
        edited_message: Optional[dict] = None,
        channel_post: Optional[dict] = None,
        edited_channel_post: Optional[dict] = None,
        inline_query: Optional[dict] = None,
        chosen_inline_result: Optional[dict] = None,
        callback_query: Optional[dict] = None,
        shipping_query: Optional[dict] = None,
        pre_checkout_query: Optional[dict] = None,
        poll: Optional[dict] = None,
        poll_answer: Optional[dict] = None,
        my_chat_member: Optional[dict] = None,
        chat_member: Optional[dict] = None,
        chat_join_request: Optional[dict] = None,
    ):
        """
        Represents an incoming update.

        Args:
            update_id (int): The update's unique identifier.
            message (Optional[Message]): New incoming message of any kind.
            edited_message (Optional[Message]): New version of a message that was edited.
            channel_post (Optional[Message]): New incoming channel post of any kind.
            edited_channel_post (Optional[Message]): New version of a channel post that was edited.
            inline_query (Optional[InlineQuery]): New incoming inline query.
            chosen_inline_result (Optional[ChosenInlineResult]): Result of an inline query chosen by a user.
            callback_query (Optional[CallbackQuery]): New incoming callback query.
            shipping_query (Optional[ShippingQuery]): New incoming shipping query.
            pre_checkout_query (Optional[PreCheckoutQuery]): New incoming pre-checkout query.
            poll (Optional[Poll]): New poll state.
            poll_answer (Optional[PollAnswer]): User changed their answer in a non-anonymous poll.
            my_chat_member (Optional[ChatMemberUpdated]): The bot's chat member status was updated.
            chat_member (Optional[ChatMemberUpdated]): A chat member's status was updated.
            chat_join_request (Optional[ChatJoinRequest]): A request to join the chat has been sent.
        """
        self.update_id = update_id
        if message:
            message["from_user"] = message.pop("from")
            self.message = Message(**message)

        # self.edited_message = Message(**edited_message)
        # self.channel_post = Message(**channel_post)
        # self.edited_channel_post = Message(**edited_channel_post)
        # self.inline_query = inline_query
        # self.chosen_inline_result = chosen_inline_result
        if callback_query:
            callback_query["from_user"] = callback_query.pop("from")
            self.callback_query = CallbackQuery(**callback_query)
        # self.shipping_query = shipping_query
        # self.pre_checkout_query = pre_checkout_query
        # self.poll = Poll(**poll)
        # self.poll_answer = PollAnswer(**poll_answer)
        # self.my_chat_member = ChatMemberUpdated(**my_chat_member)
        # self.chat_member = ChatMemberUpdated(**chat_member)
        # self.chat_join_request = ChatJoinRequest(**chat_join_request)
