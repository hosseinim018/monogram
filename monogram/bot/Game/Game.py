from typing import List

class PhotoSize:
    def __init__(self, file_id: str, width: int, height: int):
        """
        Represents the size of a photo.

        :param file_id: The unique identifier of the photo file
        :param width: The width of the photo
        :param height: The height of the photo
        """
        self.file_id = file_id
        self.width = width
        self.height = height

class MessageEntity:
    def __init__(self, type: str, offset: int, length: int):
        """
        Represents a special entity in a message.

        :param type: The type of the entity
        :param offset: The offset position of the entity in the message text
        :param length: The length of the entity in the message text
        """
        self.type = type
        self.offset = offset
        self.length = length

class Animation:
    def __init__(self, file_id: str, width: int, height: int):
        """
        Represents an animation.

        :param file_id: The unique identifier of the animation file
        :param width: The width of the animation
        :param height: The height of the animation
        """
        self.file_id = file_id
        self.width = width
        self.height = height

class Game:
    def __init__(
        self,
        title: str,
        description: str,
        photo: List[PhotoSize],
        text: str = None,
        text_entities: List[MessageEntity] = None,
        animation: Animation = None
    ):
        """
        Represents a game.

        :param title: The title of the game
        :param description: The description of the game
        :param photo: A list of PhotoSize objects representing the photos of the game
        :param text: Optional. A brief description of the game or high scores included in the game message.
                     Can be automatically edited to include current high scores for the game when the bot calls
                     setGameScore or manually edited using editMessageText. Must be between 0-4096 characters.
        :param text_entities: Optional. A list of MessageEntity objects representing special entities that appear
                              in the text, such as usernames, URLs, bot commands, etc.
        :param animation: Optional. An Animation object representing the animation that will be displayed in the
                          game message in chats. Upload via BotFather.
        """
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation