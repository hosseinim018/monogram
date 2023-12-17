from monogram import Monogram, validate_payload


class reopenGeneralForumTopic(Monogram):
    def __new__(cls, chat_id):
        """
        Use this method to reopen a closed 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights.
        The topic will be automatically unhidden if it was hidden.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='reopenGeneralForumTopic', data=payload, res=True)
        return response.json()