"""
Exposes the library's context variables
"""
from contextvars import ContextVar

Request = ContextVar('request')
Session = ContextVar('session')
(Config := ContextVar('config')).set(None)
