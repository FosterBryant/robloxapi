class NotFound(Exception):
    """Raised when something is not found"""
    pass


class BadStatus(Exception):
    """Raised when a status != 200"""
    pass


class NotAuthenticated(Exception):
    """Raised when a user is not authenticated"""
    pass
