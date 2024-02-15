from monogram import Monogram, validate_payload


class createForumTopic(Monogram):
    def __new__(cls, chat_id, name, icon_color=None, icon_custom_emoji_id=None):
        """
        Use this method to create a topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights.
        Returns information about the created topic as a ForumTopic object.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param name: Topic name, 1-128 characters
        :param icon_color: Color of the topic icon in RGB format. Currently, must be one of the allowed values
        :param icon_custom_emoji_id: Unique identifier of the custom emoji shown as the topic icon
        :return: Information about the created topic as a ForumTopic object
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="createForumTopic", data=payload, res=True)
        return response.json()
