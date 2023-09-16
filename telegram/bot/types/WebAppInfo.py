class WebAppInfo:
    """
    Describes a Web App.
    """
    def __init__(self, url: str):
        """
        Initialize a WebAppInfo object.

        :param url: An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps.
        """
        self.url = url
