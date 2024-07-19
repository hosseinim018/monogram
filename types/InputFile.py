import os
from django.conf import settings

class InputFile:
    """
    Represents the contents of a file to be uploaded.
    """

    def __init__(self, file_path: str, file_name: str = None):
        """
        Initialize an InputFile object.

        Args:
            file_path (str): The path to the file to be uploaded.
            file_name (str, optional): The name of the file. If not provided, the original file name will be used.
        """
        self.file_path = settings.BASE_DIR / file_path
        self.file_name = file_name or self._extract_file_name(file_path)
    @staticmethod
    def _extract_file_name(file_path: str) -> str:
        """
        Extract the file name from the given file path.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The extracted file name.
        """
        return os.path.basename(file_path)
