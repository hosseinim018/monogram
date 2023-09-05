from typing import Optional, Union

def edit_message_media(
    media: dict,
    chat_id: Optional[Union[int, str]] = None,
    message_id: Optional[int] = None,
    inline_message_id: Optional[str] = None,
    reply_markup: Optional[dict] = None,
) -> Union[bool, dict]:
    """
    Use this method to edit animation, audio, document, photo, or video messages.
    If a message is part of a message album, then it can be edited only to an audio for audio albums,
    only to a document for document albums, and to a photo or a video otherwise.
    When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id
    or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned,
    otherwise True is returned.

    :param chat_id: Required if inline_message_id is not specified.
                    Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified.
                       Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified.
                              Identifier of the inline message
    :param media: A JSON-serialized object for a new media content of the message
    :param reply_markup: A JSON-serialized object for a new inline keyboard.
    :return: If the edited message is not an inline message, the edited Message is returned,
             otherwise True is returned.
    """
    # Your implementation here
    pass