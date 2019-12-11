from utils import fileio
from utils import text as text_utils

cuss_all = set(fileio.load_all_cusses())


def detect_cuss(message):
    """
    Detects the cuss words present in the message.
    TODO: handle the remaining cases when transliteration module is ready.
    """
    message = message.strip().lower()
    detected = []

    if message in cuss_all:
        detected.append(message)
    else:
        message = list(text_utils.words(message))
        words = [text_utils.reduce_word(w) for w in message]

        bigrams = text_utils.ngrams(words, 2)
        trigrams = text_utils.ngrams(words, 3)

        # Creates non-spaced words
        other_hacks = []
        for i in range(2, len(words) + 1):
            other_hacks += text_utils.ngrams(words, i, "")

        words = set(words + bigrams + trigrams + other_hacks)
        for word in words:
            cuss_flag = word in cuss_all
            # if text_utils.is_hindi_word(word):
            #     translits = transliterations(word)
            #     cuss_flag = any([w for w in translits if w in cuss_all])

            if cuss_flag:
                detected.append(word)

    return detected or None
