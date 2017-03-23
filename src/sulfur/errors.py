class ValidationError(Exception):
    """
    Raised when HTML document is invalid.
    """


class DoesNotAcceptInputError(ValueError):
    """
    Exception raised on operations that tries to send input to invalid elements.
    """


class NotFoundError(object):
    """
    Error for failed queries.
    """