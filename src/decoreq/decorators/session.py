"""
Exposes the session decorator.
"""
import typing as t
from contextvars import ContextVar

from decoreq.context import Session
from .base import BaseDecoreqDecorator


class SessionDecorator(BaseDecoreqDecorator):
    """
    A session decorator that can be extended by other decoraters should they rely on a context with a session.
    """

    def context_variables(self) -> t.Iterable[t.Tuple[ContextVar, t.Any]]:
        """
        Creates the session for the current context
        :return: A list of context variables and their values
        :type: List[Tuple[ContextVar, Any]]
        """
        return super().context_variables() + [
            (Session, 10)
        ]
