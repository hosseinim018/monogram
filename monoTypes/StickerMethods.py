from typing import List, Optional, Union
from .Message import Message
from .File import File
from .Sticker import Sticker
from .StickerSet import StickerSet
from .InputSticker import InputSticker
from .MaskPosition import MaskPosition
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .ReplyKeyboardMarkup import ReplyKeyboardMarkup
from .ReplyKeyboardRemove import ReplyKeyboardRemove
from .ForceReply import ForceReply
from .ReplyParameters import ReplyParameters

class StickerMethods:
    @staticmethod
    def send_sticker(
        chat_id: Union[int, str],
        sticker: Union[str, object],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        allow_paid_broadcast: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None
    ) -> Message:
        """Send a sticker to a chat.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
            sticker: Sticker to send (file_id, URL, or file object)
            business_connection_id: Optional. Unique identifier for the target business connection
            message_thread_id: Optional. Unique identifier for the target message thread
            emoji: Optional. Emoji associated with the sticker
            disable_notification: Optional. Send message silently
            protect_content: Optional. Protect content from forwarding/saving
            allow_paid_broadcast: Optional. Allow broadcasting to large chats for a fee
            message_effect_id: Optional. Message effect ID for private chats
            reply_parameters: Optional. Parameters for replying to messages
            reply_markup: Optional. Additional interface options

        Returns:
            Message: The sent message
        """
        return Message()  # Implementation will be done in the network layer

    @staticmethod
    def get_sticker_set(name: str) -> StickerSet:
        """Get a sticker set"""
        return StickerSet()

    @staticmethod
    def get_custom_emoji_stickers(custom_emoji_ids: List[str]) -> List[Sticker]:
        """Get information about custom emoji stickers"""
        return []

    @staticmethod
    def upload_sticker_file(
        user_id: int,
        sticker: object,
        sticker_format: str
    ) -> File:
        """Upload a sticker file"""
        return File()

    @staticmethod
    def create_new_sticker_set(
        user_id: int,
        name: str,
        title: str,
        stickers: List[InputSticker],
        sticker_type: str = None,
        needs_repainting: bool = None
    ) -> bool:
        """Create a new sticker set"""
        return True

    @staticmethod
    def add_sticker_to_set(
        user_id: int,
        name: str,
        sticker: InputSticker
    ) -> bool:
        """Add a new sticker to a set"""
        return True

    @staticmethod
    def set_sticker_position_in_set(
        sticker: str,
        position: int
    ) -> bool:
        """Move a sticker in a set to a specific position"""
        return True

    @staticmethod
    def delete_sticker_from_set(sticker: str) -> bool:
        """Delete a sticker from a set"""
        return True

    @staticmethod
    def replace_sticker_in_set(
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker
    ) -> bool:
        """Replace a sticker in a set"""
        return True

    @staticmethod
    def set_sticker_emoji_list(
        sticker: str,
        emoji_list: List[str]
    ) -> bool:
        """Change the emoji list of a sticker"""
        return True

    @staticmethod
    def set_sticker_keywords(
        sticker: str,
        keywords: Optional[List[str]] = None
    ) -> bool:
        """Change search keywords of a sticker"""
        return True

    @staticmethod
    def set_sticker_mask_position(
        sticker: str,
        mask_position: Optional[MaskPosition] = None
    ) -> bool:
        """Change the mask position of a mask sticker"""
        return True

    @staticmethod
    def set_sticker_set_title(
        name: str,
        title: str
    ) -> bool:
        """Set the title of a sticker set"""
        return True

    @staticmethod
    def set_sticker_set_thumbnail(
        name: str,
        user_id: int,
        thumbnail: Union[str, object] = None,
        format: str = None
    ) -> bool:
        """Set the thumbnail of a sticker set"""
        return True

    @staticmethod
    def set_custom_emoji_sticker_set_thumbnail(
        name: str,
        custom_emoji_id: Optional[str] = None
    ) -> bool:
        """Set the thumbnail of a custom emoji sticker set"""
        return True

    @staticmethod
    def delete_sticker_set(name: str) -> bool:
        """Delete a sticker set"""
        return True
