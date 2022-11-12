"""
Exposes the headers decorators.
"""
import typing as t

from .session import SessionDecorator


class HeadersDecorator(SessionDecorator):
    """
    Use this decorator to enrich your session with additional headers.
    """
    _headers: t.Mapping[str, str]

    def __init__(self, **headers: str):
        """
        Initialize the decorator
        :param headers: The headers to add to the session
        :type headers: str
        """
        self._headers = headers
        super().__init__()


class HeaderDecorator(HeadersDecorator):
    """
    Use this decorator to enrich your session with an additional header.
    """

    def __init__(self, header: str, value: str):
        """
        Initialize the decorator
        :param header: The header to add to the session
        :type header: str
        :param value: The value of the header
        :type value: str
        """
        super().__init__(**{header: value})
