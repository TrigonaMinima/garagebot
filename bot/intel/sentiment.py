

def sentiment(text):
    """
    Takes in a text and returns 0 or 1 based on the negative or positive
    sentiment of the sentence
    TODO: insert a sentiment detecter module instead of keyword based
          sentiment detection.
    """
    text = text.lower()
    text = text.split()

    pos_sentiment = set(
        ["good", "nice", "eyy", 'attaboy', "sweet", "awesome"])
    neg_sentiment = set(
        ["no", "tatti", "oh", "wot", "wot?", "nope", "bad", "sad"])

    senti = -1
    if len(pos_sentiment.intersection(text)) > 0:
        senti = 1
    elif len(neg_sentiment.intersection(text)) > 0:
        senti = 0
    return senti
