from monogram import Monogram, validate_payload

class unpinAllGeneralForumTopicMessages(Monogram):
    def __new__(cls, chat_id):
        """
        Use this method to clear the list of pinned messages in a General forum topic.
        The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='unpinAllGeneralForumTopicMessages', data=payload, res=True)
        return response.json()