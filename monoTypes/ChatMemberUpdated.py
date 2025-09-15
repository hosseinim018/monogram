from .Chat import Chat
from .User import User
from .ChatMember import ChatMember
from .ChatInviteLink import ChatInviteLink
from .baseType import BaseType

class ChatMemberUpdated(BaseType):
    """
    This class represents changes in the status of a chat member.
    """

    def __init__(
        self,
        chat: Chat,
        date: int,
        old_chat_member: ChatMember,
        new_chat_member: ChatMember,
        invite_link: ChatInviteLink = None,
        via_chat_folder_invite_link: bool = False,
        *args,
        **kwargs,
    ):
        """
        Initialize a ChatMemberUpdated object.

        Args:
            chat (Chat): The chat the user belongs to.
            from_user (User): The performer of the action, which resulted in the change.
            date (int): The date the change was done in Unix time.
            old_chat_member (ChatMember): Previous information about the chat member.
            new_chat_member (ChatMember): New information about the chat member.
            invite_link (ChatInviteLink, optional): The chat invite link used by the user to join the chat. Only
                applicable for joining by invite link events. Defaults to None.
            via_chat_folder_invite_link (bool, optional): True if the user joined the chat via a chat folder invite
                link. Defaults to False.
        """
        super().__init__(**kwargs)
        self.chat = chat
        self.from_user = User(**self.from_user) if self.from_user else None
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_chat_folder_invite_link = via_chat_folder_invite_link
