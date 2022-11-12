"""
Exposes helper functions around context management
"""
import typing as t
from contextvars import copy_context
from functools import partial

_T = t.TypeVar('_T')
_P = t.ParamSpec('_P')


def with_new_context(func: t.Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> _T:
    """
    Runs a callable on a new managed scope.

    The new scope inherits any context from the parent scope.

    The new scope can modify a context variable that is shared with the parent scope.

    If new context variables are introduced on the new scope, they are going to be released at the end of the scope
    :param func: The function to execute on the new scope
    :type func: Callable[P, T]
    :param args: The function's positional arguments
    :type args: P.args
    :param kwargs: The function's keyword arguments
    :type kwargs: P.kwargs
    :return: The function's return value
    :rtype: T
    """
    return copy_context().run(partial(func, *args, **kwargs))


def current_context() -> t.Mapping[str, t.Any]:
    """
    Returns all variables in the current context
    :return: A mapping of all the variables and their values
    :rtype: Mapping[str, Any]
    """
    return {var.name: value for var, value in copy_context().items()}
