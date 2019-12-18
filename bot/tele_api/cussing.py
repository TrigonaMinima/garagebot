import telegram

from telegram import Update
from telegram.ext import CallbackContext

from api.cussing import CussCommandAPI as api
from utils.decs import restricted
from utils.db.logging import log_bot_reply


def bot_reply_and_log(update, reply, quote=False, **args):
    bot_reply = update.message.reply_text(reply, **args, quote=quote)
    log_bot_reply(bot_reply)


class CussCommand(object):

    @staticmethod
    @restricted
    def cuss(update: Update, context: CallbackContext):
        to_user = " ".join(context.args).strip()
        from_user = update.effective_user.username
        reply = api.cuss(from_user, to_user)
        bot_reply_and_log(update, reply)

    @staticmethod
    @restricted
    def vulgar(update: Update, context: CallbackContext):
        userid = str(update.effective_user.id)
        reply = api.vulgar(userid)

        bot_reply_and_log(update, reply, quote=False,
                          parse_mode=telegram.ParseMode.MARKDOWN)
