from telegram import Update
from telegram.ext import CallbackContext

from utils.decs import restricted
from utils.db.logging import log_bot_reply
from api.generic import GenericCommandAPI as api


def bot_reply_and_log(update, reply, quote=False, **args):
    bot_reply = update.message.reply_text(reply, **args, quote=quote)
    log_bot_reply(bot_reply)


class GenericCommand(object):
    """
    Class containing static methods of generic commands.
    """

    @staticmethod
    @restricted
    def start(update: Update, context: CallbackContext):
        """
        Handler for the "/start" command
        """
        starter = api.start()
        bot_reply_and_log(update, starter)

    @staticmethod
    @restricted
    def fetch_key_val(update: Update, context: CallbackContext):
        """
        Handler for the "/fetch" command
        """
        args = context.args
        val = api.fetch_key_val(args)
        bot_reply_and_log(
            update, val, quote=False, disable_web_page_preview=True
        )

    @staticmethod
    @restricted
    def add_key_val(update: Update, context: CallbackContext):
        """
        Handler for the "/add" command
        """
        args = context.args
        reply = api.add_key_val(args)
        bot_reply_and_log(update, reply)

    @staticmethod
    @restricted
    def pop_key_val(update: Update, context: CallbackContext):
        """
        Handler for the "/pop" command
        """
        args = context.args
        reply = api.pop_key_val(args)
        bot_reply_and_log(update, reply)

    @staticmethod
    @restricted
    def random_highlight(update: Update, context: CallbackContext):
        """
        Return random highlight.
        """
        reply = api.random_highlight()
        bot_reply_and_log(update, reply)

    @staticmethod
    @restricted
    def fuck_the_tables(update: Update, context: CallbackContext):
        """
        Copied from the fuckthetables bot on Reddit.
        """
        reply = api.fuck_the_tables()
        bot_reply_and_log(update, reply)

    @staticmethod
    @restricted
    def respect_the_tables(update: Update, context: CallbackContext):
        """
        Opposite of the fuckthetables bot. This one respects the tables.
        """
        reply = api.respect_the_tables()
        bot_reply_and_log(update, reply)
