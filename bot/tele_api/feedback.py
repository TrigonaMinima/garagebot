from telegram import Update
from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db import logging
from utils.decs import restricted_no_logging
from api.feedback import FeedbackHandlerAPI as api


class FeedbackButtons(object):
    """
    Class for feedback buttons. The option, `callback_data` decides what will
    sent back once the button is clicked.

    1 means that the correction is right
    0 means that the word is new and hence the correction is wrong
    2 means that the correction is wrong
    """

    @staticmethod
    def correction_feedback_button(button_tracker):
        """
        Creates the feedback keyboard for a correction
        """
        keyboard = [[
            InlineKeyboardButton(
                "\U0001F44D", callback_data=f'1_{button_tracker}'),
            InlineKeyboardButton(
                "\U00002795", callback_data=f'0_{button_tracker}'),
            InlineKeyboardButton(
                "\U0001F44E", callback_data=f'2_{button_tracker}'),
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup


class FeedbackHandler(object):
    """
    All functions to handle feedback
    """

    @staticmethod
    @restricted_no_logging
    def correction_feedback(update: Update, context: CallbackContext):
        """
        Gets the feedback from the button and then
        1. If correction is right then removes the inline keyboard, adds the
           correction to the eval set.
        2. if word is not in vocab, removes the correction altogether
           and adds the word to the vocab list
        3. Else, deletes the correction from the conversation and
           adds the wrong correction to the wrong correction file for
           later consideration

        Feedback will be in the from of `option_timestamp_userid` where
        `option` - 0, 1, 2;
        `timestamp` - timestamp of the reply for which corrections were made
        `userid` - the user who had sent the reply

        the `timestamp` and `userid` is given in the `monitor.Monitor()` where
        the buttons are made.
        """
        query = update.callback_query
        message_id = query.message.message_id
        chat_id = query.message.chat.id

        options = query.data
        correction = query.message.text
        feedback = api.correction_feedback(options, correction)

        # timestamp and userid were added when the buttons were created
        # in monitor.Monitor()
        timestamp, user = options.split("_")[1:]

        if feedback == 1:
            context.bot.editMessageReplyMarkup(
                message_id=message_id,
                chat_id=chat_id,
                reply_markup=None
            )
        elif feedback == 0:
            context.bot.deleteMessage(message_id=message_id, chat_id=chat_id)
            logging.update_wrong_correction(timestamp, user, correction)
        elif feedback == 2:
            context.bot.deleteMessage(message_id=message_id, chat_id=chat_id)
            logging.update_wrong_correction(timestamp, user, correction)
