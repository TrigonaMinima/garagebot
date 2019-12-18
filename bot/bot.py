import logging

from telegram.ext import (
    CommandHandler,
    Updater,
    MessageHandler, Filters,
    CallbackQueryHandler
)

from checks import check
from utils import date as date_utils
from utils.fileio import config
from tele_api.stats import Stats
from tele_api.monitor import Monitor
from tele_api.cussing import CussCommand
from tele_api.generic import GenericCommand
from tele_api.feedback import FeedbackHandler

# from stats import Stats


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


group0_handlers = [
    CommandHandler(config["CMDS"]["start"], GenericCommand.start),
    CommandHandler(
        config["CMDS"]["fetch"], GenericCommand.fetch_key_val, pass_args=True),
    CommandHandler(
        config["CMDS"]["add"], GenericCommand.add_key_val, pass_args=True),
    CommandHandler(
        config["CMDS"]["pop"], GenericCommand.pop_key_val, pass_args=True),
    CommandHandler(config["CMDS"]["fuck_tab"], GenericCommand.fuck_the_tables),
    CommandHandler(
        config["CMDS"]["respect_tab"], GenericCommand.respect_the_tables),
    CommandHandler(
        config["CMDS"]["highlight"], GenericCommand.random_highlight),
    CommandHandler(config["CMDS"]["cuss"], CussCommand.cuss, pass_args=True),
    CommandHandler(config["CMDS"]["vulgar"], CussCommand.vulgar),
    MessageHandler(Filters.text, Monitor.monitor),
]

# group1_handlers = []

crons = [
    {
        "func": Stats.weekly_cussing,
        "interval": date_utils.week_delta,
        "first": date_utils.closest_monday
    }, {
        "func": Stats.gen_wordcloud,
        "interval": date_utils.week_delta,
        "first": date_utils.closest_tuesday
    }, {
        "func": Stats.weekly_commands,
        "interval": date_utils.week_delta,
        "first": date_utils.closest_wednesday
    }, {
        "func": Stats.weekly_quotes,
        "interval": date_utils.week_delta,
        "first": date_utils.closest_thursday
    }
]


def error_callback(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    bot_token = config["TOKENS"]["bot_token"]
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    updater.dispatcher.add_handler(
        CallbackQueryHandler(FeedbackHandler.correction_feedback))

    for handler in group0_handlers:
        dp.add_handler(handler, group=0)

    # for handler in group1_handlers:
    #     dp.add_handler(handler, group=1)

    # setup periodic stats
    for cron_job in crons:
        cron = cron_job["func"]
        interval = cron_job["interval"]
        first = cron_job["first"]
        updater.job_queue.run_repeating(cron, interval=interval, first=first)

    # closest_sunday = helpers.get_next_closest_day("sunday")
    # updater.job_queue.run_repeating(
    #     Stats.weekly_messages, interval=week_delta, first=closest_sunday)

    print("All handlers initiated.")

    dp.add_error_handler(error_callback)

    updater.start_polling()
    print("Bot started")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    check()
    main()
