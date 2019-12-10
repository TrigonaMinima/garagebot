from social.yt import YT
from utils import fileio
from utils.text import words


hard_repl = fileio.load_hard_replies()


class MonitorAPI(object):
    @staticmethod
    def monitor(text, from_user):
        replies = {}
        meta = {}

        if MonitorAPI.scream(text):
            replies["scream"] = f"@{from_user}{hard_repl['scream']['default']}"

        match = YT.get_yt_links(text)
        if match:
            vid_id = match.groups()[0]
            vid_duration = YT.yt_vid_reply_duration(vid_id)
            reply = MonitorAPI.watch_youtube(vid_duration)
            replies["yt"] = reply
            meta["yt"] = vid_duration

        return replies, meta

    @staticmethod
    def scream(text):
        text_words = list(words(text))
        return text.isupper() and len(text_words) > 2

    @staticmethod
    def watch_youtube(vid_duration):
        if vid_duration == -1:
            vid_duration = 1
            reply = hard_repl["yt"]["default_n1"]
        elif not vid_duration:
            vid_duration = 1
            reply = hard_repl["yt"]["default_n2"]
        else:
            reply = hard_repl["yt"]["default_y"]
        return reply
