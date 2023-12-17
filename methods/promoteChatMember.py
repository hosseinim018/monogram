from typing import Union, Optional
from monogram import Monogram, validate_payload

class promoteChatMember(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Pass False for all boolean parameters to demote a user.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :param is_anonymous: Pass True if the administrator's presence in the chat is hidden
        :param can_manage_chat: Pass True if the administrator can access the chat event log, chat statistics, message statistics in channels,
                                see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
        :param can_post_messages: Pass True if the administrator can create channel posts, channels only
        :param can_edit_messages: Pass True if the administrator can edit messages of other users and can pin messages, channels only
        :param can_delete_messages: Pass True if the administrator can delete messages of other users
        :param can_manage_video_chats: Pass True if the administrator can manage video chats
        :param can_restrict_members: Pass True if the administrator can restrict, ban or unban chat members
        :param can_promote_members: Pass True if the administrator can add new administrators with a subset of their own privileges
                                    or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him)
        :param can_change_info: Pass True if the administrator can change chat title, photo and other settings
        :param can_invite_users: Pass True if the administrator can invite new users to the chat
        :param can_pin_messages: Pass True if the administrator can pin messages, supergroups only
        :param can_manage_topics: Pass True if the user is allowed to create, rename, close, and reopen forum topics, supergroups only
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='promoteChatMember', data=payload, res=True)
        return response.json()
