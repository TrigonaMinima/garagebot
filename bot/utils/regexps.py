import re


std_strings = re.compile(
    r"""\b[ha]+\b|\bha+t{2,}\b""",
    re.IGNORECASE
)

url_regex = re.compile(
    r"https?:\/\/[a-zA-Z0-9\./\-=_\)\(\*&\^%\$#@!<>\?{},|\+:~\[\]]+|\
            www\.[a-zA-Z0-9\./\-=_\)\(\*&\^%\$#@!<>\?{},|\+\:~[\]]+"
)

reddit_regex = re.compile(r"^/?[ur]/[a-z]+| /?[ur]/[a-z]+")
twitter_regex = re.compile(r"[@#][A-Za-z0-9_-]+")
email_regex = re.compile(
    r"[a-zA-Z0-9_\.\+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-\.]+")

space_regex = re.compile(r"  +")
number_junk_regex = re.compile(r"\b[0-9]+\b|_+")

# Diacritics handled using the code from this SO answer:
# https://stackoverflow.com/a/9524664/2650427
words_regex = re.compile(r"""
    [a-z]+[a-z\\-]*-+[a-z\\-]*[a-z]+|    
    [\w\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+['-]?
        [\w\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+|
    [\w\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+
""", re.VERBOSE)
numeric_word_regex = re.compile(r"\b[0-9][a-zA-Z0-9]+\b|\b[a-zA-Z0-9]+[0-9]\b")

# Regex for youtube links, gives video id as selected group
# https://stackoverflow.com/a/26491375/2650427
yt_reg = re.compile(r"""
    (?:.+?)?(?:\/v\/|
    watch\/|\?v=|\&v=|
    youtu\.be\/|\/v=|
    ^youtu\.be\/)([a-zA-Z0-9_-]{11})+
""", re.IGNORECASE | re.VERBOSE)


str_replace = {
    "too": re.compile(r"\bto{3,}\b", re.IGNORECASE),
    "lol": re.compile(r"\bl+o{2,}l+\b", re.IGNORECASE),
    "no": re.compile(r"\bno{2,}\b", re.IGNORECASE),
    "cool": re.compile(r"\bc+o{2,}l+\b", re.IGNORECASE),
    "funnay": re.compile(r"\bfun{3,}ay\b", re.IGNORECASE),
    "boo": re.compile(r"\bbo{2,}\b", re.IGNORECASE),
    "eww": re.compile(r"\bew{2,}\b", re.IGNORECASE),
    "toh": re.compile(r"\bto{2,}h+\b", re.IGNORECASE),
    "dayum": re.compile(r"\bdayum{2,}\b", re.IGNORECASE),
    "fuck": re.compile(r"\bfuck{2,}\b", re.IGNORECASE),
    "fod": re.compile(r"\bfod{2,}\b", re.IGNORECASE),
    "yo": re.compile(r"\byo{2,}\b", re.IGNORECASE),
    "hurr": re.compile(r"\bhurr{2,}\b", re.IGNORECASE),
    "nahin": re.compile(r"\bnahin{2,}\b", re.IGNORECASE),
    "yiss": re.compile(r"\byiss{2,}\b", re.IGNORECASE),
    "ohh": re.compile(r"\boh[hj]{1,}\b", re.IGNORECASE),
    "feeel": re.compile(r"\bfe{3,}l\b", re.IGNORECASE),
}
