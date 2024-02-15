from monogram import Monogram, validate_payload


class closeForumTopic(Monogram):
    def __new__(cls, chat_id, message_thread_id):
        """
        Use this method to close an open topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights,
        unless it is the creator of the topic.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param message_thread_id: Unique identifier for the target message thread of the forum topic
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="closeForumTopic", data=payload, res=True)
        return response.json()
