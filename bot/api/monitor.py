import random
import pysnooper

from social.yt import YT
from utils import fileio, text as text_utils
from intel.abuse import detect_cuss
from intel.sentiment import sentiment
from intel.spell import StatSpellCorrector


corrector = StatSpellCorrector()
hard_repl = fileio.load_hard_replies()


class MonitorAPI(object):
    @staticmethod
    def monitor(message, from_user):
        replies = {}
        meta = {}

        if message is None:
            return replies, meta

        # get spelling corrections
        corrections = MonitorAPI.spell_correct(message)
        if corrections:
            meta["spell"] = corrections
            replies["spell"] = []
            for (w, w_correct) in corrections:
                replies["spell"].append(f"s/{w}/{w_correct}")

        # detects cussing words
        cuss_detected = detect_cuss(message)
        if cuss_detected is None:
            cuss_detected = []
        if corrections:
            for (_, w_correct) in corrections:
                if detect_cuss(w_correct):
                    cuss_detected.append(w_correct)
        if cuss_detected:
            meta["cuss"] = list(set(cuss_detected))

        # dont scream
        if MonitorAPI.scream(message):
            replies["scream"] = f"@{from_user}{hard_repl['scream']['default']}"

        # watching the video
        match = YT.get_yt_links(message)
        if match:
            vid_id = match.groups()[0]
            vid_duration = YT.yt_vid_reply_duration(vid_id)
            reply = MonitorAPI.watch_youtube(vid_duration)
            replies["yt"] = reply
            meta["yt"] = vid_duration

        # bot's reaction when talked to
        senti = sentiment(message)
        if senti >= 0:
            replies["sentiment"] = MonitorAPI.bot_sentiment(senti)

        return replies, meta

    @staticmethod
    def scream(text):
        text_words = list(text_utils.words(text))
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

    @staticmethod
    def bot_sentiment(senti):
        reply = ""
        if senti == 0:
            reply = random.choice(fileio.load_neg_rep())
        elif senti == 1:
            reply = random.choice(fileio.load_pos_rep())
        return reply

    @staticmethod
    def spell_correct(message):
        corrections = []

        words = text_utils.words(message)
        for word in words:
            if not text_utils.valid_word(word):
                continue

            w_correct = corrector.correction(word)
            if word and w_correct:
                corrections.append((word, w_correct))

        return corrections
