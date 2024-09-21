"""
This type stub file was generated by pyright.
"""

"""
Utilities for dealing with text encodings
"""
def get_stream_enc(stream, default=...): # -> None:
    """Return the given stream's encoding or a default.

    There are cases where ``sys.std*`` might not actually be a stream, so
    check for the encoding attribute prior to returning it, and return
    a default if it doesn't exist or evaluates as False. ``default``
    is None if not provided.
    """
    ...

def getdefaultencoding(prefer_stream=...):
    """Return IPython's guess for the default encoding for bytes as text.

    If prefer_stream is True (default), asks for stdin.encoding first,
    to match the calling Terminal, but that is often None for subprocesses.

    Then fall back on locale.getpreferredencoding(),
    which should be a sensible platform default (that respects LANG environment),
    and finally to sys.getdefaultencoding() which is the most conservative option,
    and usually UTF8 as of Python 3.
    """
    ...

DEFAULT_ENCODING = ...
