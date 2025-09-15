class WebAppInfo:
    """
    Describes a Web App.
    """
    def __new__(cls, url: str, *args, **kwargs) -> dict:
        """
        Initialize a WebAppInfo object.

        :param url: An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps.
        """
        web_app = {
            'url': url,
        }
        return web_app