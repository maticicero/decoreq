"""
Exposes the base decoreq decorator class.

Every decoreq decorator needs to inherit from this class.
"""
import sys
import typing as t
from abc import ABC
from contextvars import ContextVar
from functools import partial, wraps

from decoreq.context import with_new_context, current_context

_T = t.TypeVar('_T')
_P = t.ParamSpec('_P')


class BaseDecoreqDecorator(ABC):
    """
    Base class for decoreq decorators.

    Override the `context_variables` if new context variables are required.
    """
    _func: t.Optional[t.Callable[_P, _T]]
    _owned_variables: t.List[t.Any]

    def __init__(self, func: t.Optional[t.Callable[_P, _T]] = None):
        """
        Either initializes the decorator or applies it to a function (if no initialization is required)
        :param func: The function to be decorated, if the decorator doesn't need to be initialized
        :type func: Optional[Callable[P, T]]
        """
        self._func = func
        self._owned_variables = []

    # noinspection PyMethodMayBeStatic
    def context_variables(self) -> t.List[t.Tuple[ContextVar, t.Any]]:
        """
        Override this method to create the necessary context variables for this decorator and downstream ones.
        :return: A list of context variables and their values
        :type: List[Tuple[ContextVar, Any]]
        """
        return []

    # noinspection PyMethodMayBeStatic
    def intercept(self) -> None:
        """
        Override this method to add extra logic right before calling the decorated function.
        """
        for var, value in self.context_variables():
            if var.name not in current_context():
                var.set(value)
                self._owned_variables.append(value)

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T:
        def _new_context(*fargs: _P.args, **fkwargs: _P.kwargs):
            self.intercept()
            self._func(*fargs, **fkwargs)

        if self._func is None:
            self._func = t.cast(t.Callable[_P, _T], args[0])

            @wraps(self._func)
            def _wrapper(*fargs: _P.args, **fkwargs: _P.kwargs):
                return with_new_context(partial(_new_context, *fargs, **fkwargs))

            return _wrapper
        return with_new_context(partial(_new_context, *args, **kwargs))

    # Unfortunately there doesn't seem to be a smarter way to dispose of allocated resources
    # Rather than to wait for GC to swipe through the decorator
    def __del__(self):
        for var in self._owned_variables:
            if hasattr(var, '__exit__'):
                var.__exit__(*sys.exc_info())
            elif hasattr(var, 'close') and isinstance(var.close, t.Callable):
                var.close()
