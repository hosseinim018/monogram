from monogram import Monogram, validate_payload


class editForumTopic(Monogram):
    def __new__(cls, chat_id, message_thread_id, name=None, icon_custom_emoji_id=None):
        """
        Use this method to edit the name and icon of a topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights,
        unless it is the creator of the topic.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param message_thread_id: Unique identifier for the target message thread of the forum topic
        :param name: New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept
        :param icon_custom_emoji_id: New unique identifier of the custom emoji shown as the topic icon.
                                     Use getForumTopicIconStickers to get all allowed custom emoji identifiers.
                                     Pass an empty string to remove the icon. If not specified, the current icon will be kept
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="editForumTopic", data=payload, res=True)
        return response.json()
