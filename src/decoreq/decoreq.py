"""
Exposes the primary interface of the library.
"""
from .context import ContextVariableProvider


class _Decoreq(metaclass=ContextVariableProvider):
    """
    Main interface for context variables.
    """
    pass


decoreq = _Decoreq
