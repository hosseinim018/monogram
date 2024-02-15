from typing import Union, Optional
from monogram import Monogram, validate_payload
from monogram.types import ChatPermissions


class restrictChatMember(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
        until_date: Optional[int] = None,
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup.
        The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights.
        Pass True for all permissions to lift restrictions from a user.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param user_id: Unique identifier of the target user
        :param permissions: A JSON-serialized object for new user permissions
        :param use_independent_chat_permissions: Pass True if chat permissions are set independently.
                                                  Otherwise, the can_send_other_messages and can_add_web_page_previews permissions
                                                  will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos,
                                                  can_send_videos, can_send_video_notes, and can_send_voice_notes permissions;
                                                  the can_send_polls permission will imply the can_send_messages permission.
        :param until_date: Date when restrictions will be lifted for the user; Unix time.
                           If the user is restricted for more than 366 days or less than 30 seconds from the current time,
                           they are considered to be restricted forever.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="restrictChatMember", data=payload, res=True)
        return response.json()
