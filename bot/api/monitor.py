from utils import fileio
from utils.text import words


hard_repl = fileio.load_hard_replies()


class MonitorAPI(object):
    @staticmethod
    def monitor(text, from_user):
        replies = {}
        if MonitorAPI.scream(text):
            replies["scream"] = f"@{from_user}{hard_repl['scream']['default']}"

        return replies

    @staticmethod
    def scream(text):
        text_words = list(words(text))
        return text.isupper() and len(text_words) > 2
