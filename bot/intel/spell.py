import re

from utils import modelio
from utils import text as text_utils


class StatSpellCorrector():
    def __init__(self):
        self.WORDS = modelio.load_spell_model()
        self.N = sum(self.WORDS.values())
        print("> Spelling correction model loaded")

    def update(self, words):
        self.WORDS.update(words)
        self.N = sum(self.WORDS.values())

    def case_of(self, word):
        """
        Return the case-function appropriate for word: upper, lower, title,
        or just str.
        """
        return (str.upper if word.isupper() else
                str.lower if word.islower() else
                str.title if word.istitle() else
                str)

    def P(self, word):
        """
        Probability of "word".
        """
        return self.WORDS[word] / self.N

    def candidates(self, word):
        """
        Generate possible spelling corrections for word.
        """
        return (
            self.known([word]) or
            self.known(self.edits1(word)) or
            self.known(self.edits2(word)) or [word]
        )

    def known(self, words):
        """
        The subset of words that appear in the dictionary of WORDS.
        """
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word):
        """
        All edits that are one edit away from "word".
        """
        letters = "abcdefghijklmnopqrstuvwxyz'-"
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        """
        All edits that are two edits away from "word".
        """
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if len(e2) > 2)

    def morphology(self, word, w_correct):
        """
        Checks if the correction is just a plural or other form of the
        same word. Determines the root word then add the suffix/prefix and
        check with the original word and the correction.
        """
        suffixes = [r"ly$", r"es$", r"ed$", r"ing$",
                    r"al$", r"'s$", r"s$", r"ness$", r"ise$", r"ize$"]
        for suffix in suffixes:
            if re.sub(suffix, "", word) == w_correct or \
                    re.sub(suffix, "", w_correct) == word:
                return True

        prefixes = [r"^re", r"^un", r"^in"]
        for prefix in prefixes:
            if re.sub(prefix, "", word) == w_correct:
                return True
            elif re.sub(prefix, "", w_correct) == word:
                return True

        uk_to_us = {
            r"zed$": "sed",
            r"zation$": "sation",
            r"sing$": "zing"
        }
        for prefix in uk_to_us:
            rep = uk_to_us[prefix]
            if re.sub(prefix, rep, word) == re.sub(prefix, rep, w_correct):
                return True

        return False

    def correction_(self, word):
        """
        Most probable spelling correction for word.
        TODO: How will it be implemented when we also take a context (n words
        before and n words after) along with the word
        """
        top_candidates = self.candidates(word)
        top_candidates = list(filter(lambda x: len(x) > 1, top_candidates))
        if top_candidates:
            return max(top_candidates, key=self.P)
        else:
            return word

    def correction(self, word):
        """
        Takes care of some edge cases and returns source formatted string
        - Ignore the numerics
        - Ignores the same form of the word
        - ignore multiple lettered spellings
        """
        if not word or word.isnumeric():
            return ""
        elif word.endswith("'s"):
            # Handle this properly
            w_correct = self.correction_(word[:-2].lower())
            if w_correct:
                w_correct += "'s"
        else:
            w_correct = self.correction_(word.lower())

        if word.lower() == w_correct.lower():
            return ""
        elif self.morphology(word.lower(), w_correct):
            return ""
        else:
            return self.case_of(word)(w_correct)
