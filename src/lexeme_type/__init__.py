"""Lexeme: a str subclass treating singular and plural spellings as equal."""

import importlib.metadata
import logging

try:
    __version__ = importlib.metadata.version(__package__ or __name__)
except importlib.metadata.PackageNotFoundError:
    # Raised when the distribution is not installed, e.g. when importing
    # straight out of a source checkout. importlib.metadata itself is stdlib
    # on every Python this package supports (>=3.11), so it cannot be missing.
    logging.debug(
        "Could not set __version__: %s is not installed.",
        __package__ or __name__,
    )
