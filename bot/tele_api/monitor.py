import threading

from telegram import Update
from telegram.ext import CallbackContext

from utils import fileio
from utils.decs import restricted
from utils.db.logging import log_bot_reply
from api.monitor import MonitorAPI as api


def bot_reply_and_log(update, reply, quote=False, **args):
    bot_reply = update.message.reply_text(reply, **args, quote=quote)
    log_bot_reply(bot_reply)


class Monitor(object):

    @staticmethod
    @restricted
    def monitor(update: Update, context: CallbackContext):
        userid = str(update.effective_user.id)
        username = str(update.effective_user.username)
        current_message = update.message.text

        replies, meta = api.monitor(current_message, username)

        if "scream" in replies:
            reply = replies["scream"]
            bot_reply_and_log(update, reply, quote=True)

        if "yt" in replies:
            reply = replies["yt"]
            wait_duration = meta["yt"]
            t = threading.Timer(
                wait_duration,
                bot_reply_and_log,
                args=[update, reply, True]
            )
            t.start()
