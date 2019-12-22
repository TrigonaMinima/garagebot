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


class ConfigItemMissing(Error):
    def __init__(self, config_var):
        msg = (
            f"Config variable ({config_var}) is required. "
            "Update the config.ini file to proceed."
        )
        self.message = msg
