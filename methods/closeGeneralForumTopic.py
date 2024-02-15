from monogram import Monogram, validate_payload


class closeGeneralForumTopic(Monogram):
    def __new__(cls, chat_id):
        """
        Use this method to close an open 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(
            cls, method="closeGeneralForumTopic", data=payload, res=True
        )
        return response.json()
