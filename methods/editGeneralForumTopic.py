from monogram import Monogram, validate_payload


class editGeneralForumTopic(Monogram):
    def __new__(cls, chat_id, name):
        """
        Use this method to edit the name of the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param name: New topic name, 1-128 characters
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(
            cls, method="editGeneralForumTopic", data=payload, res=True
        )
        return response.json()
