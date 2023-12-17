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
