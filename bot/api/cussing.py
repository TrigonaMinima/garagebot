import random

from utils import fileio


singular_cusses = fileio.load_singular_cusses()
bot_aliases = fileio.load_bot_alias()


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
    def vulgar():
        pass


def random_cuss():
    """Returns random gaali"""
    return random.choice(singular_cusses)
