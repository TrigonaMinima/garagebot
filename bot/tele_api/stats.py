from telegram import Update
from telegram.ext import CallbackContext

from api.stats import StatsAPI as api
from utils.db.logging import log_bot_reply


def bot_reply_and_log(update: Update, reply, quote=False, **args):
    bot_reply = update.message.reply_text(reply, **args, quote=quote)
    log_bot_reply(bot_reply)


class Stats(object):

    @staticmethod
    def gen_wordcloud(update: Update, context: CallbackContext):
        """
        Replies with the wordcloud image on the group.
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
