"""
Exposes the primary decorator for the library.
"""
from decoreq.context import ContextVariableProvider
from .base import BaseDecoreqDecorator


class Decoreq(BaseDecoreqDecorator, metaclass=ContextVariableProvider):
    """
    Serves both as decorator and context variable provider.
    """
    pass
