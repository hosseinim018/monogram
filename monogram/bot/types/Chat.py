from typing import Optional, List, Dict

class Chat:
    """Represents a chat."""

    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[bool] = None,
        photo: Optional[str] = None,
        active_usernames: Optional[List[str]] = None,
        emoji_status_custom_emoji_id: Optional[str] = None,
        emoji_status_expiration_date: Optional[int] = None,
        bio: Optional[str] = None,
        has_private_forwards: Optional[bool] = None,
        has_restricted_voice_and_video_messages: Optional[bool] = None,
        join_to_send_messages: Optional[bool] = None,
        join_by_request: Optional[bool] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional[str] = None,
        permissions: Optional[Dict[str, bool]] = None,
        slow_mode_delay: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_aggressive_anti_spam_enabled: Optional[bool] = None,
        has_hidden_members: Optional[bool] = None,
        has_protected_content: Optional[bool] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[bool] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional[str] = None
    ):
        """
        Initialize the Chat object.

        Args:
            id (int): Unique identifier for this chat.
            type (str): Type of chat, can be either "private", "group", "supergroup", or "channel".
            title (str, optional): Title, for supergroups, channels, and group chats.
            username (str, optional): Username, for private chats, supergroups, and channels if available.
            first_name (str, optional): First name of the other party in a private chat.
            last_name (str, optional): Last name of the other party in a private chat.
            is_forum (bool, optional): True, if the supergroup chat is a forum (has topics enabled).
            photo (str, optional): Chat photo. Returned only in getChat.
            active_usernames (List[str], optional): List of all active chat usernames; for private chats, supergroups, and channels. Returned only in getChat.
            emoji_status_custom_emoji_id (str, optional): Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat.
            emoji_status_expiration_date (int, optional): Expiration date of the emoji status of the other party in a private chat in Unix time, if any. Returned only in getChat.
            bio (str, optional): Bio of the other party in a private chat. Returned only in getChat.
            has_private_forwards (bool, optional): True, if privacy settings of the other party in the private chat allow using tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
            has_restricted_voice_and_video_messages (bool, optional): True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat.
            join_to_send_messages (bool, optional): True, if users need to join the supergroup before they can send messages. Returned only in getChat.
            join_by_request (bool, optional): True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.
            description (str, optional): Description, for groups, supergroups, and channel chats. Returned only in getChat.
            invite_link (str, optional): Primary invite link, for groups, supergroups, and channel chats. Returned only in getChat.
            pinned_message (str, optional): The most recent pinned message (by sending date). Returned only in getChat.
            permissions (Dict[str, bool], optional): Default chat member permissions, for groups and supergroups. Returned only in getChat.
            slow_mode_delay (int, optional): For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds. Returned only in getChat.
            message_auto_delete_time (int, optional): The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
            has_aggressive_anti_spam_enabled (bool, optional): True, if aggressiveanti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat.
            has_hidden_members (bool, optional): True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat.
            has_protected_content (bool, optional): True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
            sticker_set_name (str, optional): For supergroups, name of the group sticker set. Returned only in getChat.
            can_set_sticker_set (bool, optional): True, if the bot can change the group sticker set. Returned only in getChat.
            linked_chat_id (int, optional): Unique identifier for the linked chat, i.e., the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
            location (str, optional): For supergroups, the location to which the supergroup is connected. Returned only in getChat.
        """
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.photo = photo
        self.active_usernames = active_usernames
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.linked_chat_id = linked_chat_id
        self.location = location

        payload = {
            'id': id,
            'type': type,
            'title': title
        }

        if username is not None:
            payload['username'] = username
        if first_name is not None:
            payload['first_name'] = first_name
        if last_name is not None:
            payload['last_name'] = last_name
        if is_forum is not None:
            payload['is_forum'] = is_forum
        if photo is not None:
            payload['photo'] = photo
        if active_usernames is not None:
            payload['active_usernames'] = active_usernames
        if emoji_status_custom_emoji_id is not None:
            payload['emoji_status_custom_emoji_id'] = emoji_status_custom_emoji_id
        if emoji_status_expiration_date is not None:
            payload['emoji_status_expiration_date'] = emoji_status_expiration_date
        if bio is not None:
            payload['bio'] = bio
        if has_private_forwards is not None:
            payload['has_private_forwards'] = has_private_forwards
        if has_restricted_voice_and_video_messages is not None:
            payload['has_restricted_voice_and_video_messages'] = has_restricted_voice_and_video_messages
        if join_to_send_messages is not None:
            payload['join_to_send_messages'] = join_to_send_messages
        if join_by_request is not None:
            payload['join_by_request'] = join_by_request
        if description is not None:
            payload['description'] = description
        if invite_link is not None:
            payload['invite_link'] = invite_link
        if pinned_message is not None:
            payload['pinned_message'] = pinned_message
        if permissions is not None:
            payload['permissions'] = permissions
        if slow_mode_delay is not None:
            payload['slow_mode_delay'] = slow_mode_delay
        if message_auto_delete_time is not None:
            payload['message_auto_delete_time'] = message_auto_delete_time
        if has_aggressive_anti_spam_enabled is not None:
            payload['has_aggressive_anti_spam_enabled'] = has_aggressive_anti_spam_enabled
        if has_hidden_members is not None:
            payload['has_hidden_members'] = has_hidden_members
        if has_protected_content is not None:
            payload['has_protected_content'] = has_protected_content
        if sticker_set_name is not None:
            payload['sticker_set_name'] = sticker_set_name
        if can_set_sticker_set is not None:
            payload['can_set_sticker_set'] = can_set_sticker_set
        if linked_chat_id is not None:
            payload['linked_chat_id'] = linked_chat_id
        if location is not None:
            payload['location'] = location
