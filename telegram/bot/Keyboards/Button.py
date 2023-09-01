from typing import List, Optional
# keyboard = {
#     'inline_keyboard': [[
#         {
#             'text': button_text,
#             # 'url': button_url,
#             'web_app': {'url':'https://google.com'}
#         }
#     ]]
# }

class CallbackQuery:
    """
    This object represents an incoming callback query from a callback button in an inline keyboard.
    """
    def __init__(self, id: str, from_user: 'User', message: Optional['Message'] = None,
                 inline_message_id: Optional[str] = None, chat_instance: str = None,
                 data: Optional[str] = None, game_short_name: Optional[str] = None):
        """
        Initialize a CallbackQuery object.

        :param id: Unique identifier for this query.
        :param from_user: The sender of the query.
        :param message: Optional. Message with the callback button that originated the query.
                        Note that message content and message date will not be available if the message is too old.
        :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
        :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent.
                              Useful for high scores in games.
        :param data: Optional. Data associated with the callback button.
                     Be aware that the message originated the query can contain no callback buttons with this data.
        :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game.
        """
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name


class WebAppInfo:
    """
    Describes a Web App.
    """
    def __init__(self, url: str):
        """
        Initialize a WebAppInfo object.

        :param url: An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps.
        """
        self.url = url

class KeyboardButtonRequestUser:
    """
    This object defines the criteria used to request a suitable user.
    """
    def __init__(self, request_id: int, user_is_bot: Optional[bool] = None, user_is_premium: Optional[bool] = None):
        """
        Initialize a KeyboardButtonRequestUser object.

        :param request_id: Signed 32-bit identifier of the request, which will be received back in the UserShared object. Must be unique within the message.
        :param user_is_bot: Optional. Pass True to request a bot, pass False to request a regular user. If not specified, no additional restrictions are applied.
        :param user_is_premium: Optional. Pass True to request a premium user, pass False to request a non-premium user. If not specified, no additional restrictions are applied.
        """
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium


class KeyboardButtonRequestChat:
    """
    This object defines the criteria used to request a suitable chat.
    """
    def __init__(self, request_id: int, chat_is_channel: bool, chat_is_forum: Optional[bool] = None,
                 chat_has_username: Optional[bool] = None, chat_is_created: Optional[bool] = None,
                 user_administrator_rights: Optional['ChatAdministratorRights'] = None,
                 bot_administrator_rights: Optional['ChatAdministratorRights'] = None,
                 bot_is_member: Optional[bool] = None):
        """
        Initialize a KeyboardButtonRequestChat object.

        :param request_id: Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message.
        :param chat_is_channel: Boolean indicating if the chat should be a channel.
        :param chat_is_forum: Optional. Boolean indicating if the chat should be a forum.
        :param chat_has_username: Optional. Boolean indicating if the chat should have a username.
        :param chat_is_created: Optional. Boolean indicating if the chat should be created.
        :param user_administrator_rights: Optional. The administrator rights required for a user in the chat.
        :param bot_administrator_rights: Optional. The administrator rights required for the bot in the chat.
        :param bot_is_member: Optional. Boolean indicating if the bot should be a member of the chat.
        """
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member


class KeyboardButtonPollType:
    """
    This object represents the type of a poll.
    """
    def __init__(self, type: Optional[str] = None):
        """
        Initialize a KeyboardButtonPollType object.

        :param type: Optional. The type of the poll.
        """
        self.type = type


class KeyboardButton:
    """
    This object represents one button of the reply keyboard.
    """
    def __init__(self, text: str, request_user: Optional['KeyboardButtonRequestUser'] = None,
                 request_chat: Optional['KeyboardButtonRequestChat'] = None,
                 request_contact: Optional[bool] = None, request_location: Optional[bool] = None,
                 request_poll: Optional['KeyboardButtonPollType'] = None, web_app: Optional['WebAppInfo'] = None):
        """
        Initialize a KeyboardButton object.

        :param text: The label text on the button.
        :param request_user: Optional. The criteria used to request a user when the button is pressed.
        :param request_chat: Optional. The criteria used to request a chat when the button is pressed.
        :param request_contact: Optional. Boolean indicating if the user's contact information should be requested.
        :param request_location: Optional. Boolean indicating if the user's location should be requested.
        :param request_poll: Optional. The type of poll to be created when the button is pressed.
        :param web_app: Optional. Information about the web app to be opened when the button is pressed.
        """
        self.text = text
        self.request_user = request_user
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app


class ReplyKeyboardMarkup:
    """
    This object represents a custom keyboard with reply options.
    """
    def __init__(self, keyboard: List[List['KeyboardButton']], is_persistent: Optional[bool] = False,
                 resize_keyboard: Optional[bool] = False, one_time_keyboard: Optional[bool] = False,
                 input_field_placeholder: Optional[str] = None, selective: Optional[bool] = None):
        """
        Initialize a ReplyKeyboardMarkup object.

        :param keyboard: The list of button rows in the keyboard.
        :param is_persistent: Optional. Boolean indicating if the keyboard is persistent.
        :param resize_keyboard: Optional. Boolean indicating if the keyboard should be resized.
        :param one_time_keyboard: Optional. Boolean indicating if the keyboard should be shown only once.
        :param input_field_placeholder: Optional. The placeholder text to display in the input field.
        :param selective: Optional. Boolean indicating if the keyboard should be selective.
        """
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective


class ReplyKeyboardRemove:
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard.
    """
    def __init__(self, remove_keyboard: bool = True, selective: Optional[bool] = None):
        """
        Initialize a ReplyKeyboardRemove object.

        :param remove_keyboard: Boolean indicating if the custom keyboard should be removed.
        :param selective: Optional. Boolean indicating if the removal should be selective.
        """
        self.remove_keyboard = remove_keyboard
        self.selective = selective


class InlineKeyboardButton:
    """
    This object represents one button of an inline keyboard.
    """
    def __init__(self, text: str, url: Optional[str] = None, callback_data: Optional[str] = None,
                 web_app: Optional['WebAppInfo'] = None, login_url: Optional['LoginUrl'] = None,
                 switch_inline_query: Optional[str] = None, switch_inline_query_current_chat: Optional[str] = None,
                 switch_inline_query_chosen_chat: Optional['SwitchInlineQueryChosenChat'] = None,
                 callback_game: Optional['CallbackGame'] = None, pay: Optional[bool] = None):
        """
        Initialize an InlineKeyboardButton object.

        :param text: The label text on the button.
        :param url: Optional. The URL to open when the button is pressed.
        :param callback_data: Optional. The callback data to be sent when the button is pressed.
        :param web_app: Optional. Information about the web app to be opened when the button is pressed.
        :param login_url: Optional. The login URL to authenticate the user when the button is pressed.
        :param switch_inline_query: Optional. The inline query string to be sent when the button is pressed.
        :param switch_inline_query_current_chat: Optional. The inline query string to be sent when the button is pressed in the current chat.
        :param switch_inline_query_chosen_chat: Optional. The inline query string to be sent when the button is pressed in a chosen chat.
        :param callback_game: Optional. Information about the callback game to be played when the button is pressed.
        :param pay: Optional. Boolean indicating if the button is for a payment.
        """
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.callback_game = callback_game
        self.pay = pay


class InlineKeyboardMarkup:
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    """
    def __init__(self, inline_keyboard: List[List['InlineKeyboardButton']]):
        """
        Initialize an InlineKeyboardMarkup object.

        :param inline_keyboard: The list of button rows in the inline keyboard.
        """
        self.inline_keyboard = inline_keyboard


