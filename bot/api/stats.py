import wordcloud

from pathlib import Path

from utils import text
from utils import date as date_utils
from utils import fileio
from utils.db import queries


class StatsAPI(object):

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

        reply = {
            "wc_file": wc_file,
            "group_id": fileio.config["META"]["group_id"],
            "reply": "<WORDCLOUD>"
        }
        return reply
