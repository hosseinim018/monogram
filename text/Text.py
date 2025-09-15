from typing import Union, List

def add_tags(tag: str, text: str) -> str:
    """
    Adds a specified tag at the start and end of the given text.

    Parameters:
    tag (str): The tag to be added. It should be a string.
    text (str): The text to be tagged. It should be a string.

    Returns:
    str: The tagged text, with the specified tag added at the start and end.

    Example:
    >>> add_tags('<i>', 'Python')
    '<i>Python<i>'
    """
    return f"<{tag}>{text}</{tag}>"

def Spoiler(text: str) -> str:
    """
    The Spoiler function takes a string and returns the same string wrapped in
    a &lt;span&gt; tag with class &quot;tg-spoiler&quot;. This is used to hide text from view until
    the user clicks on it. The text will be hidden by default, but can be shown by
    clicking on the spoiler button.

    :param text: str: Specify the text that will be hidden
    :return: A string with the text in a spoiler tag
    :doc-author: Trelent
    """
    return add_tags('tg-spoiler', text)

def Bold(text: str) -> str:
    """
    The Bold function takes a string and returns the same string wrapped in
    bold tags.


    :param text: str: Specify the type of data that will be passed to the function
    :return: A string with the text wrapped in a &lt;b&gt; tag
    :doc-author: Trelent
    """
    return add_tags('b', text)

def Italic(text: str) -> str:
    """
    The Italic function takes a string and returns the same string wrapped in
    HTML italic tags.


    :param text: str: Pass in the text that you want to be italicized
    :return: The text in italics
    :doc-author: Trelent
    """
    return add_tags('i', text)

def Mono(text: str) -> str:
    """
    The Mono function takes a string and returns it wrapped in &lt;pre&gt; tags.

    :param text: str: Pass the text to be formatted into the function
    :return: The text in a monospace font
    :doc-author: Trelent
    """
    return add_tags('pre', text)

def Strikethrough(text: str) -> str:
    """
    The Strikethrough function takes a string and returns the same string with HTML strikethrough tags around it.

    :param text: str: Pass in the text that you want to be strikethrough
    :return: The text with the tags &lt;s&gt; and &lt;/s&gt;
    :doc-author: Trelent
    """
    return add_tags('s', text)

def Underline(text: str) -> str:
    """
    The Underline function takes a string and returns the same string with
        underline tags added.

    :param text: str: Specify the text that will be underlined
    :return: A string that is the text surrounded by an underline tag
    :doc-author: Trelent
    """
    return add_tags('u', text)


def CreateLink(text: str, link: str) -> str:
    """
    Creates a hyperlink by combining the given text and link.

    Parameters:
    text (str): The text to be displayed for the hyperlink.
    link (str): The URL or link to be associated with the text.

    Returns:
    str: The formatted hyperlink.

    Example:
    >>> CreateLink('OpenAI', 'https://openai.com')
    '[OpenAI](https://openai.com)'
    """
    return f'<a href="{link}">{text}</a>'


def Hashtag(text: str) -> str:
    """
    Adds a hashtag symbol before the given text.

    Parameters:
    text (str): The text to which the hashtag symbol is added.

    Returns:
    str: The text with the hashtag symbol added.

    Example:
    >>> Hashtag('AI')
    '#AI'
    """
    return "#" + text


def Mention(text: str) -> str:
    """
    Adds an at symbol before the given text.

    Parameters:
    text (str): The text to which the at symbol is added.

    Returns:
    str: The text with the at symbol added.

    Example:
    >>> User('JohnDoe')
    '@JohnDoe'
    """
    return "@" + text

def inlineMention(text: str, id:int) -> str:
    """
    The inlineMention function takes a string and an integer as arguments.
    The function returns a string with the text argument wrapped in HTML tags,
    and the id argument inserted into the href attribute of those tags.

    :param text: str: Specify the text that will be displayed in the message
    :param id:int: Specify the user id of the mentioned user
    :return: A string
    :doc-author: Trelent
    """
    return f'<a href="tg://user?id={id}">{text}</a>'

def INIsection(section: str, description: Union[str, List[str]]) -> str:
    """
    Returns a string representation of an INI section.

    Parameters:
    section (str): The name of the section.
    description (str or list): The description of the section. If the description is a list,
        each element will be joined with a newline character.

    Returns:
    str: The formatted string representation of the section.

    Example:
    >>> INIsection('Section1', 'This is section 1')
    '[Section1]\nThis is section 1'

    Example:
    >>> INIsection('Section2', ['Line 1', 'Line 2', 'Line 3'])
    '[Section2]\nLine 1\nLine 2\nLine 3'
    """
    if isinstance(description, list):
        return f'{section}\n' + '\n'.join(description)
    else:
        return f"{section}\n{description}"
