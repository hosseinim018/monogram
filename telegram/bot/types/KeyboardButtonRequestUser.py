from typing import Optional
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
