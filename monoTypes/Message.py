from typing import Optional, List, Union, Dict, Any
from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.User import User
from monogram.monoTypes.Chat import Chat
from monogram.monoTypes.MessageEntity import MessageEntity
from monogram.monoTypes.Animation import Animation
from monogram.monoTypes.Audio import Audio
from monogram.monoTypes.Document import Document
from monogram.monoTypes.PhotoSize import PhotoSize
from monogram.monoTypes.Sticker import Sticker
from monogram.monoTypes.Video import Video
from monogram.monoTypes.VideoNote import VideoNote
from monogram.monoTypes.Voice import Voice
from monogram.monoTypes.Contact import Contact
from monogram.monoTypes.Location import Location
from monogram.monoTypes.Poll import Poll
from monogram.monoTypes.Invoice import Invoice
from monogram.monoTypes.SuccessfulPayment import SuccessfulPayment
from monogram.text import format_text


class Message(BaseType):
    def __init__(
        self,
        message_id: int,
        date: int,
        chat: dict,
        bot: Any = None,
        text: Optional[str] = None,
        # from_user: Optional[Dict] = None,
        forward_from: Optional[Dict] = None,
        forward_from_chat: Optional[Dict] = None,
        forward_from_message_id: Optional[int] = None,
        forward_signature: Optional[str] = None,
        forward_sender_name: Optional[str] = None,
        forward_date: Optional[int] = None,
        reply_to_message: Optional[Dict] = None,
        via_bot: Optional[Dict] = None,
        edit_date: Optional[int] = None,
        media_group_id: Optional[str] = None,
        author_signature: Optional[str] = None,
        entities: Optional[List[Dict]] = None,
        animation: Optional[Dict] = None,
        audio: Optional[Dict] = None,
        document: Optional[Dict] = None,
        photo: Optional[List[Dict]] = None,
        sticker: Optional[Dict] = None,
        video: Optional[Dict] = None,
        video_note: Optional[Dict] = None,
        voice: Optional[Dict] = None,
        caption: Optional[str] = None,
        contact: Optional[Dict] = None,
        location: Optional[Dict] = None,
        poll: Optional[Dict] = None,
        new_chat_members: Optional[List[Dict]] = None,
        left_chat_member: Optional[Dict] = None,
        new_chat_title: Optional[str] = None,
        new_chat_photo: Optional[List[Dict]] = None,
        delete_chat_photo: bool = False,
        group_chat_created: bool = False,
        supergroup_chat_created: bool = False,
        channel_chat_created: bool = False,
        migrate_to_chat_id: Optional[int] = None,
        migrate_from_chat_id: Optional[int] = None,
        pinned_message: Optional[Dict] = None,
        invoice: Optional[Dict] = None,
        successful_payment: Optional[Dict] = None,
        connected_website: Optional[str] = None,
        passport_data: Optional[Dict] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        **kwargs: Any
    ):
        """
        Initialize a Message object that represents an incoming message in the Telegram Bot API.

        Args:
            message_id (int): Unique message identifier
            date (int): Unix timestamp of the message
            chat (dict): Chat object where the message was sent
            bot (Any, optional): Bot instance handling this message
            text (str, optional): Text content of the message
            from_user (dict, optional): User who sent the message
            forward_from (dict, optional): Original sender of a forwarded message
            forward_from_chat (dict, optional): Original chat of a forwarded message
            forward_from_message_id (int, optional): Message ID in the original chat
            forward_signature (str, optional): Signature of the post author for forwarded messages
            forward_sender_name (str, optional): Sender's name for anonymous forwards
            forward_date (int, optional): Date of original message
            reply_to_message (dict, optional): The message being replied to
            via_bot (dict, optional): Bot through which the message was sent
            edit_date (int, optional): Last edit date of the message
            media_group_id (str, optional): Group ID for grouped media messages
            author_signature (str, optional): Author's signature in channel posts
            entities (List[dict], optional): Special entities in the message text
            animation (dict, optional): Information about an animation
            audio (dict, optional): Information about an audio file
            document (dict, optional): Information about a document
            photo (List[dict], optional): Available sizes of a photo
            sticker (dict, optional): Information about a sticker
            video (dict, optional): Information about a video
            video_note (dict, optional): Information about a video note
            voice (dict, optional): Information about a voice message
            caption (str, optional): Caption for media messages
            contact (dict, optional): Information about a shared contact
            location (dict, optional): Information about a shared location
            poll (dict, optional): Information about a poll
            new_chat_members (List[dict], optional): New members added to the chat
            left_chat_member (dict, optional): Member that left the chat
            new_chat_title (str, optional): New chat title
            new_chat_photo (List[dict], optional): New chat photo
            delete_chat_photo (bool, optional): Chat photo was deleted
            group_chat_created (bool, optional): Group has been created
            supergroup_chat_created (bool, optional): Supergroup has been created
            channel_chat_created (bool, optional): Channel has been created
            migrate_to_chat_id (int, optional): Group migrated to a supergroup
            migrate_from_chat_id (int, optional): Supergroup created from a group
            pinned_message (dict, optional): Pinned message in the chat
            invoice (dict, optional): Information about an invoice
            successful_payment (dict, optional): Information about a successful payment
            connected_website (str, optional): Connected website
            passport_data (dict, optional): Telegram Passport data
            reply_markup (Union[InlineKeyboardMarkup, dict], optional): Inline keyboard attached to the message
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)
        self.message_id = message_id
        self.date = date
        self.chat = Chat(**chat)
        self.bot = bot

        # Message content
        self.text = text
        self.from_user = User(**self.from_user) if 'from_user' in self else None
        self.entities = [MessageEntity(**entity) for entity in entities] if entities else None
        self.caption = caption

        # Media content
        self.animation = Animation(**animation) if animation else None
        self.audio = Audio(**audio) if audio else None
        self.document = Document(**document) if document else None
        
        self.photo = [PhotoSize(**photo_size) for photo_size in photo] if photo else None
        self.sticker = Sticker(**sticker) if sticker else None
        self.video = Video(**video) if video else None
        self.video_note = VideoNote(**video_note) if video_note else None
        self.voice = Voice(**voice) if voice else None

        # Forward information
        self.forward_from = User(**forward_from) if forward_from else None
        self.forward_from_chat = Chat(**forward_from_chat) if forward_from_chat else None
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date

        # Reply and bot information
        self.reply_to_message = Message(**reply_to_message) if reply_to_message else None
        self.via_bot = User(**via_bot) if via_bot else None
        self.edit_date = edit_date

        # Group message attributes
        self.media_group_id = media_group_id
        self.author_signature = author_signature

        # Chat member updates
        self.new_chat_members = [User(**member) for member in new_chat_members] if new_chat_members else None
        self.left_chat_member = User(**left_chat_member) if left_chat_member else None
        self.new_chat_title = new_chat_title
        self.new_chat_photo = [PhotoSize(**photo) for photo in new_chat_photo] if new_chat_photo else None
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = Message(**pinned_message) if pinned_message else None

        # Additional features
        self.contact = Contact(**contact) if contact else None
        self.location = Location(**location) if location else None
        self.poll = Poll(**poll) if poll else None
        self.invoice = Invoice(**invoice) if invoice else None
        self.successful_payment = SuccessfulPayment(**successful_payment) if successful_payment else None
        self.connected_website = connected_website
        self.passport_data = passport_data
        # self.reply_markup = reply_markup if isinstance(reply_markup, InlineKeyboardMarkup) else InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.reply_markup = reply_markup if reply_markup else None

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            setattr(self, key, value)

    def answer(self, text: str, keyboard: Optional[Union[InlineKeyboardMarkup, Dict]] = None, 
              parse_mode: Optional[str] = 'html', disable_web_page_preview: bool = False) -> Optional[dict]:
        """
        Send a text message in response to the current message.

        Args:
            text: The text of the message to be sent
            keyboard: Optional inline keyboard markup or dict representing the keyboard
            parse_mode: Optional mode for parsing entities in the message text. 
                      Can be "HTML" or "Markdown"
            disable_web_page_preview: If True, disables link previews for links in the message

        Returns:
            Optional[dict]: The response from the Telegram API
        """
        return self.bot.sendMessage(
            chat_id=self.chat.id,
            text=format_text(text),
            reply_markup=keyboard,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview
        )

    def editMessage(self, text: str, keyboard: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
                   parse_mode: Optional[str] = 'html') -> Optional[dict]:
        """
        Edit the text and reply markup of the current message.

        Args:
            text: New text of the message
            keyboard: Optional new inline keyboard markup
            parse_mode: Optional mode for parsing entities in the message text.
                      Can be "HTML" or "Markdown"

        Returns:
            Optional[dict]: The response from the Telegram API
        """
        return self.bot.editMessageText(
            text=format_text(text),
            reply_markup=keyboard,
            chat_id=self.chat.id,
            message_id=self.message_id,
            parse_mode=parse_mode
        )

    def reply(self, text: str, keyboard: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
             parse_mode: Optional[str] = 'html', disable_web_page_preview: bool = False,
             disable_notification: bool = False) -> Optional[dict]:
        """
        Reply to the current message with a new message.

        Args:
            text: The text of the reply message
            keyboard: Optional inline keyboard markup
            parse_mode: Optional mode for parsing entities in the message text.
                      Can be "HTML" or "Markdown"
            disable_web_page_preview: If True, disables link previews
            disable_notification: If True, sends the message silently

        Returns:
            Optional[dict]: The response from the Telegram API
        """
        return self.bot.sendMessage(
            chat_id=self.chat.id,
            text=format_text(text),
            reply_to_message_id=self.message_id,
            reply_markup=keyboard,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification
        )

    def deleteMessage(self):
        """
        Deletes the current message from the chat.

        This method calls the bot's `deleteMessage` function, passing the chat ID and message ID
        of the current message instance.

        Returns:
            The result of the bot's `deleteMessage` method, which typically indicates whether
            the deletion was successful.

        Raises:
            Any exceptions raised by the underlying bot's `deleteMessage` method.
        """
        return self.bot.deleteMessage(
            chat_id=self.chat.id,
            message_id=self.message_id,
            )