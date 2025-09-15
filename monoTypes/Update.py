from typing import Optional
from .baseType import BaseType
from monogram.monoTypes import Message
from monogram.monoTypes import BusinessConnection
from monogram.monoTypes import BusinessMessagesDeleted
from monogram.monoTypes import MessageReactionUpdated
from monogram.monoTypes import MessageReactionCountUpdated
from monogram.monoTypes import InlineQuery
from monogram.monoTypes import ChosenInlineResult
from monogram.monoTypes import CallbackQuery
from monogram.monoTypes import ShippingQuery
from monogram.monoTypes import PreCheckoutQuery
from monogram.monoTypes import PaidMediaPurchased
from monogram.monoTypes import Poll
from monogram.monoTypes import PollAnswer
from monogram.monoTypes import ChatMemberUpdated
from monogram.monoTypes import ChatJoinRequest
from monogram.monoTypes import ChatBoostUpdated
from monogram.monoTypes import ChatBoostRemoved




class Update(BaseType):
    def __init__(self, bot, **kwargs):
        super().__init__(**kwargs)
        # self.update_id = update_id
        # print('update id: ', kwargs.get('update_id', 'N/A'))
        # print('inside update: ', self)
        # print('=======')
        # print(self.__dict__)
        # print('=======')
        # Dynamically set the correct optional field based on the input dictionary
        if 'message' in self:
            self.message = Message(bot=bot, **self['message'])
        elif 'edited_message' in self:
            self.edited_message = Message(bot=bot, **self['edited_message'])
        elif 'channel_post' in self:
            self.channel_post = Message(bot=bot, **self['channel_post'])
        elif 'edited_channel_post' in self:
            self.edited_channel_post = Message(bot=bot, **self['edited_channel_post'])
        elif 'business_connection' in self:
            self.business_connection = BusinessConnection(**self['business_connection'])
        elif 'business_message' in self:
            self.business_message = Message(**self['business_message'])
        elif 'edited_business_message' in self:
            self.edited_business_message = Message(bot=bot, **self['edited_business_message'])
        elif 'deleted_business_messages' in self:
            self.deleted_business_messages = BusinessMessagesDeleted(**self['deleted_business_messages'])
        elif 'message_reaction' in self:
            self.message_reaction = MessageReactionUpdated(**self['message_reaction'])
        elif 'message_reaction_count' in self:
            self.message_reaction_count = MessageReactionCountUpdated(**self['message_reaction_count'])
        elif 'inline_query' in self:
            self.inline_query = InlineQuery(**self['inline_query'])
        elif 'chosen_inline_result' in self:
            self.chosen_inline_result = ChosenInlineResult(**self['chosen_inline_result'])
        elif 'callback_query' in self:
            # For callback_query, if 'message' is present within it, also parse that
            callback_data = self['callback_query']
            if 'message' in callback_data and isinstance(callback_data['message'], dict):
                callback_data['message'] = Message(bot=bot, **callback_data['message'])
            self.callback_query = CallbackQuery(bot=bot, **callback_data)
        elif 'shipping_query' in self:
            self.shipping_query = ShippingQuery(**self['shipping_query'])
        elif 'pre_checkout_query' in self:
            self.pre_checkout_query = PreCheckoutQuery(**self['pre_checkout_query'])
        elif 'purchased_paid_media' in self:
            self.purchased_paid_media = PaidMediaPurchased(**self['purchased_paid_media'])
        elif 'poll' in self:
            self.poll = Poll(**self['poll'])
        elif 'poll_answer' in self:
            self.poll_answer = PollAnswer(**self['poll_answer'])
        elif 'my_chat_member' in self:
            # Similar to callback_query, if nested objects need parsing
            self.my_chat_member = ChatMemberUpdated(**self['my_chat_member'])
        elif 'chat_member' in self:
            self.chat_member = ChatMemberUpdated(**self['chat_member'])
        elif 'chat_join_request' in self:
            self.chat_join_request = ChatJoinRequest(**self['chat_join_request'])
        elif 'chat_boost' in self:
            self.chat_boost = ChatBoostUpdated(**self['chat_boost'])
        elif 'removed_chat_boost' in self:
            self.removed_chat_boost = ChatBoostRemoved(**self['removed_chat_boost'])


    # def get_update_type(self) -> Optional[str]:
    #     """Returns the type of the update (e.g., 'message', 'inline_query')."""
    #     type = [getattr(self, key) for key in self.__dict__.keys() if key is not 'update_id']
    #     if type is not None:
    #         return type
    #     return None
