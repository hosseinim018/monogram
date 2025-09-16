from .baseType import BaseType

class AnswerInlineQuery(BaseType):
    """
    This class represents an answer to an inline query. 
    Use this method to send answers to an inline query. On success, True is returned.
    No more than 50 results per query are allowed.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize an AnswerInlineQuery object.

        Parameters:
            inline_query_id (str): Unique identifier for the answered query
            results (list): A JSON-serializable array of results for the inline query
            cache_time (int, optional): Maximum cache time in seconds. Defaults to 300.
            is_personal (bool, optional): If True, results are cached only for the query sender
            next_offset (str, optional): Offset for the next query. Empty string if no more results
            button (InlineQueryResultsButton, optional): Button to be shown above results
        """
        super().__init__(*args, **kwargs)
        
        # Required parameters
        self.inline_query_id = kwargs.get('inline_query_id')
        self.results = kwargs.get('results', [])

        # Optional parameters with defaults
        self.cache_time = kwargs.get('cache_time', 300)
        self.is_personal = kwargs.get('is_personal', False)
        self.next_offset = kwargs.get('next_offset', '')
        self.button = kwargs.get('button', None)

    def to_dict(self):
        """
        Convert the AnswerInlineQuery object to a dictionary.
        
        Returns:
            dict: The object represented as a dictionary
        """
        data = {
            'inline_query_id': self.inline_query_id,
            'results': self.results,
            'cache_time': self.cache_time,
            'is_personal': self.is_personal,
        }

        # Add optional fields only if they are set
        if self.next_offset:
            data['next_offset'] = self.next_offset
        if self.button is not None:
            data['button'] = self.button

        return data
