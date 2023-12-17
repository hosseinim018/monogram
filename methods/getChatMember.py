from monogram import Monogram, validate_payload
class getChatMember(Monogram):
    def __new__(cls, chat_id, user_id):
        """
        Use this method to get information about a member of a chat.
        The method is only guaranteed to work for other users if the bot is an administrator in the chat.
        Returns a ChatMember object on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :return: ChatMember object on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getChatMember', data=payload, res=True)
        return response.json()
