from .Chat import Chat
from .User import User
from .Message import Message
from .Game import Game
from .CallbackGame import CallbackGame
from .GameHighScore import GameHighScore
from .GameMethods import GameMethods
from .Invoice import Invoice
from .SuccessfulPayment import SuccessfulPayment
from .BusinessConnection import BusinessConnection
from .BusinessMessagesDeleted import BusinessMessagesDeleted
from .MessageReactionUpdated import MessageReactionUpdated
from .MessageReactionCountUpdated import MessageReactionCountUpdated
from .InlineQuery import InlineQuery
from .ChosenInlineResult import ChosenInlineResult
from .ShippingQuery import ShippingQuery
from .PreCheckoutQuery import PreCheckoutQuery
from .PaidMediaPurchased import PaidMediaPurchased
from .ChatBoostUpdated import ChatBoostUpdated
from .ChatBoostRemoved import ChatBoostRemoved
from .OrderInfo import OrderInfo
from .ShippingAddress import ShippingAddress
from .ReactionType import ReactionType
from .ChatBoost import ChatBoost
from .MessageId import MessageId
from .MessageEntity import MessageEntity
from .PhotoSize import PhotoSize
from .Animation import Animation
from .Audio import Audio
from .Document import Document
from .Voice import Voice
from .Dice import Dice
from .PollOption import PollOption
from .PollAnswer import PollAnswer
from .Poll import Poll
from .Location import Location
from .Venue import Venue
from .WebAppData import WebAppData
from .ProximityAlertTriggered import ProximityAlertTriggered
from .MessageAutoDeleteTimerChanged import MessageAutoDeleteTimerChanged
from .ForumTopicCreated import ForumTopicCreated
from .ForumTopicEdited import ForumTopicEdited
from .UserShared import UserShared
from .VideoChatParticipantsInvited import VideoChatParticipantsInvited
from .VideoChatEnded import VideoChatEnded
from .WriteAccessAllowed import WriteAccessAllowed
from .VideoChatScheduled import VideoChatScheduled
from .VideoChatEnded import VideoChatEnded
from .VideoChatParticipantsInvited import VideoChatParticipantsInvited
from .UserProfilePhotos import UserProfilePhotos
from .File import File
from .WebAppInfo import WebAppInfo
from .ReplyKeyboardMarkup import ReplyKeyboardMarkup
from .KeyboardButton import KeyboardButton
from .KeyboardButtonRequestUser import KeyboardButtonRequestUser
from .KeyboardButtonRequestChat import KeyboardButtonRequestChat
from .KeyboardButtonPollType import KeyboardButtonPollType
from .ReplyKeyboardRemove import ReplyKeyboardRemove
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .InlineKeyboardButton import InlineKeyboardButton
from .LoginUrl import LoginUrl
from .SwitchInlineQueryChosenChat import SwitchInlineQueryChosenChat
from .CallbackQuery import CallbackQuery
from .ForceReply import ForceReply
from .ChatPhoto import ChatPhoto
from .ChatInviteLink import ChatInviteLink
from .ChatAdministratorRights import ChatAdministratorRights
from .ChatMember import ChatMember
from .ChatMemberOwner import ChatMemberOwner
from .ChatMemberAdministrator import ChatMemberAdministrator
from .ChatMemberMember import ChatMemberMember
from .ChatMemberRestricted import ChatMemberRestricted
from .ChatMemberLeft import ChatMemberLeft
from .ChatMemberBanned import ChatMemberBanned
from .ChatMemberUpdated import ChatMemberUpdated
from .ChatJoinRequest import ChatJoinRequest
from .ChatPermissions import ChatPermissions
from .ChatLocation import ChatLocation
from .ForumTopic import ForumTopic
from .BotCommand import BotCommand
from .BotCommandScope import BotCommandScope
from .BotCommandScopeDefault import BotCommandScopeDefault
from .BotCommandScopeAllPrivateChats import BotCommandScopeAllPrivateChats
from .BotCommandScopeAllGroupChats import BotCommandScopeAllGroupChats
from .BotCommandScopeAllChatAdministrators import BotCommandScopeAllChatAdministrators
from .BotCommandScopeChat import BotCommandScopeChat
from .BotCommandScopeChatAdministrators import BotCommandScopeChatAdministrators
from .BotCommandScopeChatMember import BotCommandScopeChatMember
from .BotName import BotName
# from .BotDescription
# from .BotShortDescription import BotShortDescription
# from .MenuButton import MenuButton
# from .MenuButtonCommands import MenuButtonCommands
from .MenuButtonWebApp import MenuButtonWebApp
from .MenuButtonDefault import MenuButtonDefault
from .ResponseParameters import ResponseParameters
from .InputMedia import InputMedia
from .InputMediaPhoto import InputMediaPhoto
from .InputMediaVideo import InputMediaVideo
from .InputMediaAnimation import InputMediaAnimation
from .InputMediaAudio import InputMediaAudio
from .InputMediaDocument import InputMediaDocument
from .InputFile import InputFile
from .ChatShared import ChatShared
from .Video import Video
from .VideoNote import VideoNote
from .Contact import Contact
from .InlineQueryResultArticle import InlineQueryResultArticle
from .InputTextMessageContent import InputTextMessageContent
from .InlineQueryResultDocument import InlineQueryResultDocument
from .InlineQueryResultLocation import InlineQueryResultLocation
from .InlineQueryResultVenue import InlineQueryResultVenue
from .InlineQueryResultCachedGif import InlineQueryResultCachedGif
from .InlineQueryResultGame import InlineQueryResultGame
from .InlineQueryResultContact import InlineQueryResultContact
from .InlineQueryResultPhoto import InlineQueryResultPhoto
from .InlineQueryResultCachedPhoto import InlineQueryResultCachedPhoto
from .InlineQueryResultCachedMpeg4Gif import InlineQueryResultCachedMpeg4Gif
from .InlineQueryResultCachedSticker import InlineQueryResultCachedSticker
from .InlineQueryResultCachedVideo import InlineQueryResultCachedVideo
from .InlineQueryResultCachedDocument import InlineQueryResultCachedDocument
from .InlineQueryResultCachedVoice import InlineQueryResultCachedVoice
from .InlineQueryResultCachedAudio import InlineQueryResultCachedAudio
from .InlineQueryResult import InlineQueryResult
from .InputLocationMessageContent import InputLocationMessageContent
from .InputVenueMessageContent import InputVenueMessageContent
from .InputContactMessageContent import InputContactMessageContent
from .InputInvoiceMessageContent import InputInvoiceMessageContent
from .PreparedInlineMessage import PreparedInlineMessage
from .answerWebAppQuery import answerWebAppQuery
from .SentWebAppMessage import SentWebAppMessage

from monogram.monoTypes import VideoChatStarted, GeneralForumTopicHidden, GeneralForumTopicUnhidden, ForumTopicReopened, \
    ForumTopicClosed, ForumTopicCreated, Story
from .baseType import BaseType
from .Update import Update

class CallbackGame:
    pass

__all__ = [
    "Update",
    "BaseType",
    "Chat",
    "User",
    "Message",
    # Game related
    "Game",
    "CallbackGame",
    "GameHighScore",
    "GameMethods",
    # Payment related
    "Invoice",
    "SuccessfulPayment",
    "OrderInfo",
    "ShippingAddress",
    # Business and Reactions
    "BusinessConnection",
    "BusinessMessagesDeleted",
    "MessageReactionUpdated",
    "MessageReactionCountUpdated",
    "ReactionType",
    # Inline related
    "InlineQuery",
    # Payment and Shipping
    "ShippingQuery",
    "PreCheckoutQuery",
    "PaidMediaPurchased",
    # Chat Boost
    "ChatBoostUpdated",
    "ChatBoostRemoved",
    "ChatBoost",
    "MessageId",
    "MessageEntity",
    "PhotoSize",
    "Animation",
    "Audio",
    "Document",
    "Story",
    "Video",
    "VideoNote",
    "Voice",
    "Contact",
    "Dice",
    "PollOption",
    "PollAnswer",
    "Poll",
    "Location",
    "Venue",
    "WebAppData",
    "ProximityAlertTriggered",
    "MessageAutoDeleteTimerChanged",
    "ForumTopicCreated",
    "ForumTopicClosed",
    "ForumTopicEdited",
    "ForumTopicReopened",
    "GeneralForumTopicHidden",
    "GeneralForumTopicUnhidden",
    "UserShared",
    "WriteAccessAllowed",
    "VideoChatScheduled",
    "VideoChatStarted",
    "VideoChatEnded",
    "VideoChatParticipantsInvited",
    "UserProfilePhotos",
    "File",
    "WebAppInfo",
    "ReplyKeyboardMarkup",
    "KeyboardButton",
    "KeyboardButtonRequestUser",
    "KeyboardButtonRequestChat",
    "KeyboardButtonPollType",
    "ReplyKeyboardRemove",
    "InlineKeyboardMarkup",
    "InlineKeyboardButton",
    "LoginUrl",
    "SwitchInlineQueryChosenChat",
    "CallbackQuery",
    "ForceReply",
    "ChatPhoto",
    "ChatInviteLink",
    "ChatAdministratorRights",
    "ChatMember",
    "ChatMemberOwner",
    "ChatMemberAdministrator",
    "ChatMemberMember",
    "ChatMemberRestricted",
    "ChatMemberLeft",
    "ChatMemberBanned",
    "ChatMemberUpdated",
    "ChatJoinRequest",
    "ChatPermissions",
    "ChatLocation",
    "ForumTopic",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeDefault",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotName",
    "BotDescription",
    "BotShortDescription",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonWebApp",
    "MenuButtonDefault",
    "ResponseParameters",
    "InputMedia",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputFile",
    "ChatShared",
    "CallbackGame",
    "InlineQueryResultArticle",
    "InputTextMessageContent",
    "InlineQueryResultAudio",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
    "InlineQueryResultDocument",
    "InlineQueryResultLocation",
    "InlineQueryResultVenue",
    "InlineQueryResultCachedGif",
    "InlineQueryResultGame",
    "InlineQueryResultContact",
    "InlineQueryResultPhoto",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultCachedAudio",
    "InlineQueryResult",
    'InputLocationMessageContent',
    'InputVenueMessageContent',
    'InputContactMessageContent',
    'InputInvoiceMessageContent',
    'ChosenInlineResult',
    'PreparedInlineMessage',
    'answerWebAppQuery',
    'SentWebAppMessage',
]

