from typing import Union
from monogram import Monogram, validate_payload

class setChatPermissions(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        permissions: dict,
        use_independent_chat_permissions: bool = False
    ) -> bool:
        """
        Use this method to set default chat permissions for all members.
        The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param permissions: A dictionary object for new default chat permissions
        :param use_independent_chat_permissions: Pass True if chat permissions are set independently.
                                                Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply
                                                the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos,
                                                can_send_video_notes, and can_send_voice_notes permissions;
                                                the can_send_polls permission will imply the can_send_messages permission.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setChatPermissions', data=payload, res=True)
        return response.json()