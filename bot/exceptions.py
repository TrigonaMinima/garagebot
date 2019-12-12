class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class DirDoesNotExist(Error):
    def __init__(self, message):
        self.message = message


class ConfigDoesNotExist(Error):
    def __init__(self):
        self.message = "config.ini does not exist in the root directory!"


class DBDoesNotExist(Error):
    def __init__(self, message):
        self.message = message


class TableDoesNotExist(Error):
    def __init__(self, message):
        self.message = message
