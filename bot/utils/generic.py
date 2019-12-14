from collections import Counter


def filter_counter_n(counter, n=1):
    """
    From the `counter`, removes all those words which have a frequency of `n`
    or less. Default `n` is `1`
    """
    freq_n_words = [
        word for word in counter if counter[word] <= n]

    for word in freq_n_words:
        counter.pop(word)
    return counter
