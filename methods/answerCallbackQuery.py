from monogram import Monogram, validate_payload


class answerCallbackQuery(Monogram):
    def __new__(
        cls,
        callback_query_id: str,
        text: str = None,
        show_alert: bool = False,
        url: str = None,
        cache_time: int = 0,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from inline keyboards.
        The answer will be displayed to the user as a notification at the top of the chat screen or as an alert.
        On success, True is returned.

        Alternatively, the user can be redirected to the specified Game URL.
        For this option to work, you must first create a game for your bot via @BotFather and accept the terms.
        Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

        :param callback_query_id: Unique identifier for the query to be answered
        :param text: Text of the notification. If not specified, nothing will be shown to the user. 0-200 characters.
        :param show_alert: If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to False.
        :param url: URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather,
                    specify the URL that opens your game. Note that this will only work if the query comes from a callback_game button.
                    Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.
        :param cache_time: The maximum amount of time in seconds that the result of the callback query may be cached client-side.
                           Telegram apps will support caching starting in version 3.14. Defaults to 0.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(
            cls, method="answerCallbackQuery", data=payload, res=True
        )
        return response.json()
