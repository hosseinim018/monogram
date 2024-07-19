from dataclasses import dataclass
from typing import Optional, List
from monogram.types import *
from monogram.methods import sendMessage
from monogram.types.PhotoSize import PhotoSize
# from monogram.UpdatingMessages import editMessageText


class Invoice:
    def __init__(self, **kwargs):
        pass


class SuccessfulPayment:
    def __init__(self, **kwargs):
        pass


@dataclass
class Message:
    def __init__(
        self,
        message_id: int,
        date: int,
        chat: dict,
        message_thread_id: Optional[int] = None,
        from_user: Optional[dict] = None,
        sender_chat: Optional[dict] = None,
        link_preview_options: Optional[dict] = None,
        forward_from: Optional[dict] = None,
        forward_origin: Optional[dict] = None,
        forward_from_chat: Optional[dict] = None,
        forward_from_message_id: Optional[int] = None,
        forward_signature: Optional[str] = None,
        forward_sender_name: Optional[str] = None,
        forward_date: Optional[int] = None,
        is_topic_message: Optional[bool] = None,
        is_automatic_forward: Optional[bool] = None,
        reply_to_message: Optional[dict] = None,
        via_bot: Optional[dict] = None,
        edit_date: Optional[int] = None,
        has_protected_content: Optional[bool] = None,
        media_group_id: Optional[str] = None,
        author_signature: Optional[str] = None,
        text: Optional[str] = None,
        entities: Optional[List] = None,
        animation: Optional[dict] = None,
        audio: Optional[dict] = None,
        document: Optional[dict] = None,
        photo: Optional[List] = None,
        sticker: Optional[dict] = None,
        story: Optional["Story"] = None,
        video: Optional[dict] = None,
        video_note: Optional[dict] = None,
        voice: Optional[dict] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List] = None,
        has_media_spoiler: Optional[bool] = None,
        contact: Optional[dict] = None,
        dice: Optional[dict] = None,
        game: Optional[dict] = None,
        poll: Optional[dict] = None,
        venue: Optional[dict] = None,
        location: Optional[dict] = None,
        new_chat_members: Optional[List] = None,
        left_chat_member: Optional[dict] = None,
        new_chat_title: Optional[str] = None,
        new_chat_photo: Optional[List] = None,
        delete_chat_photo: Optional[bool] = None,
        group_chat_created: Optional[bool] = None,
        supergroup_chat_created: Optional[bool] = None,
        channel_chat_created: Optional[bool] = None,
        message_auto_delete_timer_changed: Optional[dict] = None,
        migrate_to_chat_id: Optional[int] = None,
        migrate_from_chat_id: Optional[int] = None,
        pinned_message: Optional[dict] = None,
        invoice: Optional[dict] = None,
        successful_payment: Optional[dict] = None,
        user_shared: Optional[dict] = None,
        chat_shared: Optional[dict] = None,
        connected_website: Optional[str] = None,
        write_access_allowed: Optional[dict] = None,
        passport_data: Optional[dict] = None,
        proximity_alert_triggered: Optional[dict] = None,
        forum_topic_created: Optional[dict] = None,
        forum_topic_edited: Optional[dict] = None,
        forum_topic_closed: Optional[dict] = None,
        forum_topic_reopened: Optional[dict] = None,
        general_forum_topic_hidden: Optional[dict] = None,
        general_forum_topic_unhidden: Optional[dict] = None,
        video_chat_scheduled: Optional[dict] = None,
        video_chat_started: Optional[dict] = None,
        video_chat_ended: Optional[dict] = None,
        video_chat_participants_invited: Optional[dict] = None,
        web_app_data: Optional[dict] = None,
        reply_markup: Optional[dict] = None,
    ):
        """
          Represents an incoming message in the Telegram Bot API.

          :arg:
          - message_id (int): The unique identifier of the message.
          - from_user (User): Optional. The sender of the message.
          - date (int): The date and time the message was sent.
          - chat (Chat): The chat to which the message belongs.
          - forward_from (User): Optional. The user who sent this message originally, in case it is a forwarded message.
          - forward_from_chat (Chat): Optional. The chat from which the message was forwarded.
          - forward_from_message_id (int): Optional. The message identifier of the original message in the forwarding chat.
          - forward_signature (str): Optional. For messages forwarded from channels, the author's signature.
          - forward_sender_name (str): Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages.
          - forward_date (int): Optional. The date and time the original message was sent in the forwarding chat.
          - reply_to_message (Message): Optional. The message being replied to.
          - via_bot (User): Optional. The bot through which the message was sent.
          - edit_date (int): Optional. The date and time the message was last edited.
          - media_group_id (str): Optional. The unique identifier of a media message group this message belongs to.
          - author_signature (str): Optional. The signature of the post author for messages in channels.
          - text (str): Optional. The text of the message, if it is a text message.
          - entities (List[MessageEntity]): Optional. Special entities like usernames, URLs, etc. that appear in the text.
          - animation (Animation): Optional. The animation contained in the message, if it is an animation message.
          - audio (Audio): Optional. The audio file contained in the message, if it is an audio message.
          - document (Document): Optional. The document file contained in the message, if it is a document message.
          - photo (List[PhotoSize]): Optional. The photos attached to the message, if it is a photo message.
          - sticker (Sticker): Optional. The sticker contained in the message, if it is a sticker message.
          - video (Video): Optional. The video file contained in the message, if it is a video message.
          - video_note (VideoNote): Optional. The video note contained in the message, if it is a video note message.
          - voice (Voice): Optional. The voice message contained in the message, if it is a voice message.
          - caption (str): Optional. The caption of the message.
          - contact (Contact): Optional. The contact information contained in the message, if it is a contact message.
          - location (Location): Optional. The location information contained in the message, if it is a location message.
          - poll (Poll): Optional. The poll contained in the message, if it is a poll message.
          - new_chat_members (List[User]): Optional. New members added to the chat, if applicable.
          - left_chat_member (User): Optional. A member who left the chat, if applicable.
          - new_chat_title (str): Optional. The title of the chat was changed to this value, if applicable.
          - new_chat_photo (List[PhotoSize]): Optional. The chat photo was changed to this value, if applicable.
          - delete_chat_photo (bool): Optional. True, if the chat photo was deleted.
          - group_chat_created (bool): Optional. True, if a group chat was created.
          - supergroup_chat_created (bool): Optional. True, if a supergroup chat was created.
          - channel_chat_created (bool): Optional. True, if a channel chat was created.
          - migrate_to_chat_id (int): Optional. The supergroup or channel id to which the chat was migrated to.
          - migrate_from_chat_id (int): Optional. The group or channel id from which the chat was migrated from.
          - pinned_message (Message): Optional. The message that was pinned, if applicable.
          - invoice (Invoice): Optional. The invoice contained in the message, if it is an invoice message.
          - successful_payment (SuccessfulPayment): Optional. The payment information in a successful payment message.
          - connected_website (str): Optional. The domain name of the website connected with the message.
          - passport_data (PassportData): Optional. The passport data contained in the message, if it is a passport message.
          - reply_markup (InlineKeyboardMarkup): Optional. The inline keyboard markup attached to the message.

          Note: Not all fields are present in every message object, depending on the type of the message.
          """
        self.message_id = message_id
        self.date = date
        self.chat = Chat(**chat)
        self.message_thread_id = message_thread_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.forward_from = User(**forward_from) if forward_from else None
        self.forward_from_chat = (
            Chat(**forward_from_chat) if forward_from_chat else None
        )
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        # self.reply_to_message = (Message(**reply_to_message) if reply_to_message else reply_to_message)
        self.via_bot = User(**via_bot) if via_bot else via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.animation = Animation(**animation) if animation else animation
        self.audio = Audio(**audio) if audio else audio
        self.document = Document(**document) if document else document
        self.photo = [PhotoSize(**ph) for ph in photo] if photo else photo
        self.sticker = sticker
        self.story = story
        self.video = Video(**video) if video else video
        self.video_note = VideoNote(**video_note) if video_note else video_note
        self.voice = Voice(**voice) if voice else voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.contact = Contact(**contact) if contact else contact
        self.dice = Dice(**dice) if dice else dice
        self.game = game
        self.poll = Poll(**poll) if poll else poll
        self.venue = Venue(**venue) if venue else venue
        self.location = Location(**location) if location else location
        self.new_chat_members = new_chat_members
        self.left_chat_member = (
            User(**left_chat_member) if left_chat_member else left_chat_member
        )
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = (
            MessageAutoDeleteTimerChanged(**message_auto_delete_timer_changed)
            if message_auto_delete_timer_changed
            else None
        )
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = (
            Message(**pinned_message) if pinned_message else pinned_message
        )
        self.invoice = Invoice(**invoice) if invoice else None
        self.successful_payment = (
            SuccessfulPayment(**successful_payment) if successful_payment else None
        )
        self.user_shared = UserShared(**user_shared) if user_shared else None
        self.chat_shared = ChatShared(**chat_shared) if chat_shared else None
        self.connected_website = connected_website
        self.write_access_allowed = (
            WriteAccessAllowed(**write_access_allowed) if write_access_allowed else None
        )
        self.passport_data = passport_data
        self.proximity_alert_triggered = (
            ProximityAlertTriggered(**proximity_alert_triggered)
            if proximity_alert_triggered
            else None
        )
        self.forum_topic_created = (
            ForumTopicCreated(**forum_topic_created) if forum_topic_created else None
        )
        self.forum_topic_edited = (
            ForumTopicEdited(**forum_topic_edited) if forum_topic_edited else None
        )

        # this types not be created yet:

        # self.forum_topic_closed = ForumTopicClosed(**forum_topic_closed)
        # self.forum_topic_reopened = ForumTopicReopened(**forum_topic_reopened)
        # self.general_forum_topic_hidden = GeneralForumTopicHidden(**general_forum_topic_hidden)
        # self.general_forum_topic_unhidden = GeneralForumTopicUnhidden(**general_forum_topic_unhidden)
        # self.video_chat_scheduled = VideoChatScheduled(**video_chat_scheduled)
        # self.video_chat_started = VideoChatStarted(**video_chat_started)
        self.video_chat_ended = (
            VideoChatEnded(**video_chat_ended) if video_chat_ended else None
        )
        self.video_chat_participants_invited = (
            VideoChatParticipantsInvited(**video_chat_participants_invited)
            if video_chat_participants_invited
            else None
        )
        self.web_app_data = WebAppData(**web_app_data) if web_app_data else None
        self.reply_markup = reply_markup if reply_markup else None

    def answer(self, text: str, keyboard=None):
        if keyboard:
            sendMessage(chat_id=self.chat.id, text=text, reply_markup=keyboard)
        else:
            sendMessage(chat_id=self.chat.id, text=text)

    # def editMessage(self, text: str, keyboard=None):
    #     if keyboard:
    #         editMessageText(text=text, reply_markup=keyboard, chat_id=self.chat.id, message_id=self.message_id)
    #     else:
    #         editMessageText(text=text, chat_id=self.chat.id, message_id=self.message_id)

    def reply(self, text: str, keyboard):
        if keyboard:
            sendMessage(
                chat_id=self.chat.id,
                reply_to_message_id=self.message_id,
                text=text,
                reply_markup=keyboard,
            )
        else:
            sendMessage(
                chat_id=self.chat.id, text=text, reply_to_message_id=self.message_id
            )
