import telegram

from telegram import Update
from telegram.ext import CallbackContext

from api.stats import StatsAPI as api
from utils.db.logging import log_bot_reply


def bot_reply_and_log(update: Update, reply, quote=False, **args):
    bot_reply = update.message.reply_text(reply, **args, quote=quote)
    log_bot_reply(bot_reply)


class Stats(object):

    @staticmethod
    def weekly_cussing(update: Update, context: CallbackContext):
        """
        Sends a message to the group with the weekly cussing counts
        """
        reply_dict = api.weekly_cussing()

        bot_reply = context.bot.send_message(
            chat_id=reply_dict["group_id"],
            text=reply_dict["reply"],
            parse_mode=telegram.ParseMode.MARKDOWN
        )
        log_bot_reply(bot_reply)

    @staticmethod
    def gen_wordcloud(update: Update, context: CallbackContext):
        """
        Sends a wordcloud image on the group made from the past 30 days.
        """
        wc_dict = api.gen_wordcloud()

        wc_file = wc_dict["wc_file"]
        group_id = wc_dict["group_id"]
        reply = wc_dict["reply"]

        bot_reply = context.bot.send_photo(
            chat_id=group_id, photo=open(wc_file, 'rb'))
        bot_reply.text = reply

        wc_file.unlink()
        log_bot_reply(bot_reply)
