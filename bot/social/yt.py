import math
import urllib

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from utils.fileio import config
from utils.regexps import yt_reg


class YT(object):

    @staticmethod
    def iso_2_seconds(iso_duration):
        """
        iso_duration - ISO 8601 time format
        examples :
            'P1W2DT6H21M32S' - 1 week, 2 days, 6 hours, 21 mins, 32 secs,
            'PT7M15S' - 7 mins, 15 secs
        """
        split = iso_duration.split('T')
        period = split[0]
        time = split[1]
        timeD = {}

        # days & weeks
        if len(period) > 1:
            return -1

        # hours, minutes & seconds
        if len(time.split('H')) > 1:
            timeD['hours'] = int(time.split('H')[0])
            time = time.split('H')[1]
        if len(time.split('M')) > 1:
            timeD['minutes'] = int(time.split('M')[0])
            time = time.split('M')[1]
        if len(time.split('S')) > 1:
            timeD['seconds'] = int(time.split('S')[0])

        # convert to seconds
        timeS = timeD.get('hours', 0) * (60 * 60) + \
            timeD.get('minutes', 0) * (60) + \
            timeD.get('seconds', 0)
        return timeS

    @staticmethod
    def yt_vid_reply_duration(id):
        DEVELOPER_KEY = config["TOKENS"]["yt_api_key"]
        YOUTUBE_API_SERVICE_NAME = 'youtube'
        YOUTUBE_API_VERSION = 'v3'
        args = {
            "part": "contentDetails",
            "id": id
        }
        youtube = build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY,
            cache_discovery=False
        )
        response = youtube.videos().list(**args).execute()

        iso_time = response['items'][0]['contentDetails']['duration']
        dur = YT.iso_2_seconds(iso_time)
        if 0 < dur < 60:
            return math.floor(dur * 1.1)
        elif dur > 60:
            return dur + 10
        return dur

    @staticmethod
    def get_yt_links(text):
        text = urllib.parse.unquote(text)
        match = yt_reg.match(text)
        return match
