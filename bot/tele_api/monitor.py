import threading

from telegram import Update, MessageEntity
from telegram.ext import CallbackContext

from utils import fileio
from utils.decs import restricted_no_logging
from utils.db.logging import log_bot_reply, log_text_replies
from api.monitor import MonitorAPI as api
from tele_api.feedback import FeedbackButtons as feedback_buttons


def bot_reply_and_log(update: Update, reply, quote=False, **args):
    bot_reply = update.message.reply_text(reply, **args, quote=quote)
    log_bot_reply(bot_reply)


def is_replied_to_bot(update: Update):
    """
    Checks if current message is a reply to bot's message.
    """
    is_replied = 0
    if update.effective_message.reply_to_message:
        replied_to_msg = update.effective_message.reply_to_message
        replied_to_user = replied_to_msg.from_user.username
        if replied_to_user == fileio.config["META"]["bot_username"]:
            is_replied = 1
    return is_replied


def get_spell_feedback_buttons(update: Update):
    timestamp = update.effective_message.date.strftime("%s")
    user = update.effective_user.id
    button_tracker = f"{timestamp}_{user}"
    button_markup = feedback_buttons.correction_feedback_button(button_tracker)
    return button_markup


class Monitor(object):

    @staticmethod
    @restricted_no_logging
    def monitor(update: Update, context: CallbackContext):
        # userid = str(update.effective_user.id)
        username = str(update.effective_user.username)
        current_message = update.message.text

        # handles links when markdown like format is used
        entities = update.message.parse_entities([MessageEntity.TEXT_LINK])
        for link in entities:
            current_message += f" {link.url}"
        update.message.text = current_message

        replies, meta = api.monitor(current_message, username)
        log_text_replies(update, meta)

        if current_message is not None:
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

            if is_replied_to_bot(update) and "sentiment" in replies:
                reply = replies["sentiment"]
                bot_reply_and_log(update, reply, True)

            button_markup = get_spell_feedback_buttons(update)
            if "spell" in replies:
                for reply in replies["spell"]:
                    bot_reply_and_log(
                        update, reply, quote=False, reply_markup=button_markup)
