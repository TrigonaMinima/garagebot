import wordcloud

from pathlib import Path

from utils import text
from utils import fileio
from utils.db import queries
from utils import date as date_utils


hard_repl = fileio.load_hard_replies()
user_dict = queries.get_users()


class StatsAPI(object):

    @staticmethod
    def weekly_cussing():
        date_from, date_to = date_utils.get_from_to()
        counts = queries.get_cuss_counts(
            date_from.timestamp(), date_to.timestamp())

        if any(counts.values()):
            reply = hard_repl["weekly_cussing"]["default_y1"]
            for user in counts:
                reply += f"`{user_dict[user]:<10}` - {counts[user]}\n"
            reply += hard_repl["weekly_cussing"]["default_y2"]
        else:
            reply = hard_repl["weekly_cussing"]["default_n"]

        reply_dict = {
            "reply": reply,
            "group_id": fileio.config["META"]["group_id"]
        }
        return reply_dict

    @staticmethod
    def gen_wordcloud():
        """
        Creates a wordcloud from the past 1 months of text and sends the
        file path.
        """
        stopwords = fileio.load_stop_words()

        date_from, date_to = date_utils.get_from_to(30)
        text = queries.get_text(date_from.timestamp(), date_to.timestamp())
        text = text.words(text.lower())
        text = " ".join(text)

        wc = wordcloud.WordCloud(
            height=400,
            width=800,
            background_color="black",
            stopwords=stopwords
        )
        wc = wc.generate(text)

        data_dir = Path(fileio.config["DIR"]["data"])
        wc_file = data_dir / f"{date_to.ctime()}.png"
        wc.to_file(wc_file)

        reply_dict = {
            "wc_file": wc_file,
            "group_id": fileio.config["META"]["group_id"],
            "reply": "<WORDCLOUD>"
        }
        return reply_dict

    @staticmethod
    def weekly_commands():
        date_from, date_to = date_utils.get_from_to()
        counts = queries.get_command_counts(
            date_from.timestamp(), date_to.timestamp())

        if any(counts.values()):
            reply = hard_repl["weekly_commands"]["default_y"]
            for user in counts:
                reply += f"`{user_dict[user]:<10}` - {counts[user]}\n"
        else:
            reply = hard_repl["weekly_commands"]["default_n"]

        reply_dict = {
            "reply": reply,
            "group_id": fileio.config["META"]["group_id"]
        }
        return reply_dict

    @staticmethod
    def weekly_quotes():
        date_from, date_to = date_utils.get_from_to()
        counts = queries.get_quote_counts(
            date_from.timestamp(), date_to.timestamp())

        if any(counts.values()):
            reply = hard_repl["weekly_quotes"]["default_y"]

            for i in counts:
                reply += f"`{i[0]:<12}` -> `{i[1]:<12}` : `{i[2]}`\n"
        else:
            reply = hard_repl["weekly_quotes"]["default_n"]

        reply_dict = {
            "reply": reply,
            "group_id": fileio.config["META"]["group_id"]
        }
        return reply_dict

    @staticmethod
    def weekly_messages():
        date_from, date_to = date_utils.get_from_to()
        counts = queries.get_quote_counts(
            date_from.timestamp(), date_to.timestamp())

        if any(counts.values()):
            reply = hard_repl["weekly_messages"]["default_y"]

            for user in counts:
                reply += f"`{user_dict[user]:<10}` - {counts[user]}\n"
        else:
            reply = hard_repl["weekly_messages"]["default_n"]

        reply_dict = {
            "reply": reply,
            "group_id": fileio.config["META"]["group_id"]
        }
        return reply_dict
