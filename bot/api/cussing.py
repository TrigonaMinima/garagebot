import random

from utils import fileio
from utils.db import queries
from utils import date as date_utils


singular_cusses = fileio.load_singular_cusses()
bot_aliases = fileio.load_bot_alias()
hard_repl = fileio.load_hard_replies()
user_dict = queries.get_users()


class CussCommandAPI(object):

    @staticmethod
    def cuss(from_user, to_user):
        reply = ""
        rand_cuss = random_cuss()

        if to_user.lower().strip(" @") in bot_aliases:
            to_user = f"@{from_user}"

        reply = f"{rand_cuss.title()} {to_user}"
        return reply

    @staticmethod
    def vulgar(userid):
        date_from = date_utils.get_last_monday().timestamp()
        counts = queries.get_cuss_counts(date_from)
        print(counts)

        if any(counts.values()):
            reply = ""
            for user in counts:
                reply += f"`{user_dict[user]:<12}` -\t{counts[user]: 5}\n"
        else:
            reply = hard_repl["vulgar"]["default_n"]

        return reply


def random_cuss():
    """Returns random gaali"""
    return random.choice(singular_cusses)
