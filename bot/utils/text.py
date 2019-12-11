import unicodedata

from functools import reduce

from utils import regexps


HIN_LETTERS = set([
    "ँ", "ं", "ः", "अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ऑ", "ओ", "औ",
    "क", "ख", "ग", "घ", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ",
    "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह",
    "़", "ा", "ि", "ी", "ु", "ू", "ृ", "ॅ", "े", "ै", "ॉ", "ो", "ौ", "्"
])


def is_hindi_word(word):
    """
    Checks if a word is in raw hindi or not.
    """
    return all(map(lambda x: x in HIN_LETTERS, word))


def strip_accents(text):
    """
    - Normalizes the accented characters
    - Truncates the foreign characters
    """
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")
    text = text.decode("utf8")
    return text


def words(text):
    """
    Takes a text and returns an iterator of individual words (tokens).
    - Accented characters are normalized
    - Hindi characters are preserved
    - Other foreign characters are truncated
    """
    for word in regexps.str_replace:
        text = regexps.str_replace[word].sub(word, text)

    text = regexps.url_regex.sub("", text)
    text = regexps.std_strings.sub("", text)

    text = regexps.reddit_regex.sub("", text)
    text = regexps.email_regex.sub("", text)
    text = regexps.twitter_regex.sub("", text)

    text = regexps.number_junk_regex.sub(" ", text)
    text = regexps.numeric_word_regex.sub(" ", text)
    text = regexps.space_regex.sub(" ", text)

    words = regexps.words_regex.findall(text)
    for i, word in enumerate(words):
        if not is_hindi_word(word):
            word = strip_accents(word)
        words[i] = word
    words = filter(lambda x: 1 < len(x) < 25, words)
    return words


def reduce_word(word):
    """Converts 'reaaaaaally' to 'realy'."""
    return reduce(lambda x, y: x if x[-1] == y else x + y, word)


def ngrams(words, k, sep=" "):
    """Returns n-grams reduced."""
    n = len(words)
    if n < k:
        return []
    new_words = [sep.join(words[i:i + k]) for i in range(n - k + 1)]
    new_words = [reduce_word(word) for word in new_words]
    return new_words
