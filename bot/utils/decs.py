from functools import wraps
from telegram import Update
from telegram.ext import CallbackContext

from utils.fileio import load_users
from utils.db.logging import log_command


users = load_users()


def restricted(func):
    """
    Decorator to only allow the specific users to call the functions.
    """
    @wraps(func)
    def wrapped(update: Update, context: CallbackContext, *args, **kwargs):
        user_id = str(update.effective_user.id)
        log_command(update)
        if users and user_id not in users:
            print("Unauthorized access denied for {}.".format(user_id))
            return

        return func(update, context, *args, **kwargs)
    return wrapped
