"""
Exposes relevant decoreq decorators
"""
from .base import BaseDecoreqDecorator
from .headers import HeadersDecorator, HeaderDecorator
from .session import SessionDecorator

session = SessionDecorator
header = HeaderDecorator
headers = HeadersDecorator

__all__ = ['session', 'header', 'headers']
