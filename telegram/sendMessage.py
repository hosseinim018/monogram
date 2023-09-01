from .config import API_ENDPOINT, PROXIES, PROXY
import requests
import socks
from typing import Optional, Dict, Any


def send_message(chat_id: int, message_thread_id: Optional[int] = None, text: Optional[str] = None,
                 parse_mode: Optional[str] = None, entities: Optional[Dict[str, Any]] = None,
                 disable_web_page_preview: Optional[bool] = None, disable_notification: Optional[bool] = None,
                 protect_content: Optional[bool] = None, reply_to_message_id: Optional[int] = None,
                 allow_sending_without_reply: Optional[bool] = None, reply_markup: Optional[Dict[str, Any]] = None) -> None:
    """
    Send a text message to a chat or username of the target channel.

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel
            (in the format @channel-username).
        message_thread_id (int, optional): Unique identifier for the target message thread (topic) of the forum;
            for forum supergroups only.
        text (str, optional): Text of the message to be sent, 1-4096 characters after entity parsing.
        parse_mode (str, optional): Mode for parsing entities in the message text. See formatting options
            for more details.
        entities (Dict[str, Any], optional): A JSON-serialized list of special entities that appear in the message text,
            which can be specified instead of parse_mode.
        disable_web_page_preview (bool, optional): Disables link previews for links in this message.
        disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.
        protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving.
        reply_to_message_id (int, optional): If the message is a reply, ID of the original message.
        allow_sending_without_reply (bool, optional): Pass True if the message should be sent even if the specified
            replied-to message is not found.
        reply_markup (Dict[str, Any], optional): Additional interface options. A JSON-serialized object for an inline
            keyboard, custom reply keyboard, instructions to remove reply keyboard, or to force a reply from the user.

    Returns:
        None

    Raises:
        requests.exceptions.HTTPError: If there is an HTTP error during the request.
        requests.exceptions.RequestException: If there is a general request exception.
    """

    api_endpoint = API_ENDPOINT + "sendMessage"  # Construct the API endpoint URL

    message = {}

    if chat_id is None or text is None:
        message['error'] = 'chat_id and text are required parameters'
        return message

    message['chat_id'] = chat_id

    if message_thread_id is not None:
        message['message_thread_id'] = message_thread_id

    if text is not None:
        message['text'] = text

    if parse_mode is not None:
        message['parse_mode'] = parse_mode

    if entities is not None:
        message['entities'] = entities

    if disable_web_page_preview is not None:
        message['disable_web_page_preview'] = disable_web_page_preview

    if disable_notification is not None:
        message['disable_notification'] = disable_notification

    if protect_content is not None:
        message['protect_content'] = protect_content

    if reply_to_message_id is not None:
        message['reply_to_message_id'] = reply_to_message_id

    if allow_sending_without_reply is not None:
        message['allow_sending_without_reply'] = allow_sending_without_reply

    if reply_markup is not None:
        message['reply_markup'] = reply_markup

    try:
        # Send the request
        response = requests.post(api_endpoint, json=message, proxies=PROXIES)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        print('Message sent successfully!')

    except requests.exceptions.HTTPError as e:
        error_message = str(e)
        print(f'Failed to send message. Error message: {error_message}')

    except requests.exceptions.RequestException as e:
        error_message = str(e)
        print(f'Failed to send message. Error message: {error_message}')





import re

def format_text(text):
    """
    Formats the given text by applying various formatting styles.

    Args:
        text (str): The text to be formatted.

    Returns:
        str: The formatted text.
    """

    # Bold: *bold text*
    text = re.sub(r'\*([^*]+)\*', r'<b>\1</b>', text)

    # Italic: _italic text_
    text = re.sub(r'_([^_]+)_', r'<i>\1</i>', text)

    # Underline: __underline__
    text = re.sub(r'__(.*?)__', r'<u>\1</u>', text)

    # Strikethrough: ~strikethrough~
    text = re.sub(r'~(.*?)~', r'<s>\1</s>', text)

    # Spoiler: ||spoiler||
    text = re.sub(r'\|\|(.*?)\|\|', r'<span class="spoiler">\1</span>', text)

    # Inline URL: [inline URL](http://www.example.com/)
    text = re.sub(r'\[inline URL\]\((.*?)\)', r'<a href="\1">\1</a>', text)

    # Inline mention: [inline mention of a user](tg://user?id=123456789)
    text = re.sub(r'\[inline mention of a user\]\((.*?)\)', r'<a href="\1">@user</a>', text)

    # Emoji: ![👍](tg://emoji?id=5368324170671202286)
    text = re.sub(r'!\[(.*?)\]\(tg://emoji\?id=(.*?)\)', r'<img src="\1" alt="emoji">', text)

    # Inline fixed-width code: `inline fixed-width code`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Pre-formatted fixed-width code block: ```pre-formatted fixed-width code block```
    text = re.sub(r'```(.*?)```', r'<pre>\1</pre>', text, flags=re.DOTALL)

    # Pre-formatted fixed-width code block (Python): ```python\npre-formatted fixed-width code block written in the Python programming language\n```
    text = re.sub(r'```(.*?)```', r'<pre><code class="language-python">\1</code></pre>', text, flags=re.DOTALL)

    return text