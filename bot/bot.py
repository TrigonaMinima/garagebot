import logging

from telegram.ext import (
    CommandHandler,
    Updater,
    # CommandHandler, MessageHandler, Filters,
    #     CallbackQueryHandler
)

from checks import check
from utils.fileio import config
from tele_api.generic import GenericCommand

# import helpers
# from stats import Stats
# from mazduri import Aadesh, Ashleel, Bhasha, Mazduri
# from feedback import FeedbackHandler as FH


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


group0_handlers = [
    CommandHandler(config["CMDS"]["start"], GenericCommand.start),
    CommandHandler(
        config["CMDS"]["fetch"], GenericCommand.fetch_key_val, pass_args=True),
    # CommandHandler(config["CMDS"]["cuss"], Ashleel.gaali, pass_args=True),
    CommandHandler(
        config["CMDS"]["add"], GenericCommand.add_key_val, pass_args=True),
    CommandHandler(
        config["CMDS"]["pop"], GenericCommand.pop_key_val, pass_args=True),
    CommandHandler(
        config["CMDS"]["fuck_tables"], GenericCommand.fuck_the_tables),
    CommandHandler(
        config["CMDS"]["respect_tables"], GenericCommand.respect_the_tables),
    # CommandHandler("a", Ashleel.ashleellaundakaun),
    CommandHandler(
        config["CMDS"]["highlight"], GenericCommand.random_highlight),
    # CommandHandler("t", Bhasha.transliterate, pass_args=True),
    # CommandHandler("new", Bhasha.shabdkosh, pass_args=True),
    # MessageHandler(Filters.text, Mazduri.monitoring),
]

# group1_handlers = []


def error_callback(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    bot_token = config["TOKENS"]["bot_token"]
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    # updater.dispatcher.add_handler(
    #     CallbackQueryHandler(FH.correction_feedback))

    for handler in group0_handlers:
        dp.add_handler(handler, group=0)

    # for handler in group1_handlers:
    #     dp.add_handler(handler, group=1)

    # day_delta = helpers.get_time_delta(1)
    # week_delta = helpers.get_time_delta(7)
    # closest_monday = helpers.get_next_closest_day("monday")
    # updater.job_queue.run_repeating(
    #     Stats.weekly_gaaliya, interval=week_delta, first=closest_monday)

    # closest_tuesday = helpers.get_next_closest_day("tuesday")
    # updater.job_queue.run_repeating(
    #     Stats.gen_wordcloud, interval=week_delta, first=closest_tuesday)

    # closest_wednesday = helpers.get_next_closest_day("wednesday")
    # updater.job_queue.run_repeating(
    #     Stats.weekly_links, interval=week_delta, first=closest_wednesday)

    # closest_thursday = helpers.get_next_closest_day("thursday")
    # updater.job_queue.run_repeating(
    #     Stats.weekly_corrections, interval=week_delta, first=closest_thursday)

    # closest_friday = helpers.get_next_closest_day("friday")
    # updater.job_queue.run_repeating(
    #     Stats.weekly_commands, interval=week_delta, first=closest_friday)

    # closest_saturday = helpers.get_next_closest_day("saturday")
    # updater.job_queue.run_repeating(
    #     Stats.weekly_quotes, interval=week_delta, first=closest_saturday)

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