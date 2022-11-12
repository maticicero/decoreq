"""
Exposes a metaclass that can be used to transform a class into a context variable provider
"""
import typing as t

from .helpers import current_context


class ContextVariableProvider(type):
    """
    Allows for context variables to be fetched as normal class attributes.
    """

    def __getattr__(self, name: str) -> t.Any:
        for var, value in current_context():
            if name == var:
                return value
        raise AttributeError(name)

    def __contains__(self, name: str):
        return name in current_context()
