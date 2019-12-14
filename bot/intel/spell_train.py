import re

from collections import Counter
from pathlib import Path

from utils import fileio, modelio, generic


class StatSpellCorrectorTrain(object):

    def __init__(self):
        data_dir = Path(fileio.config["DIR"]["data"])
        models_dir = Path(fileio.config["DIR"]["models"])

        self.model_f = models_dir / fileio.config["MODEL"]["spell_f"]
        self.data_f = data_dir / fileio.config["DATA"]["spell_data_f"]
        self.new_words_f = data_dir / fileio.config["DATA"]["spell_new_f"]

        self.WORDS = None
        self.new_words = None

        if not self.new_words_f.stat().st_size == 0:
            self.prepare_model()
            self.save_counter()
        else:
            print(">> No change in the model")

    def spell_data_counter(self):
        """
        Gets word frequency dict from document text
        """
        data_counter = fileio.prepare_file_counter(self.data_f)
        print(">> Loaded spell data file.")
        return data_counter

    def new_words_counter(self):
        """
        Gets word frequency dict from new words file created from feedback.
        """
        new_words_counter = fileio.prepare_file_counter(self.new_words_f)
        print(">> Loaded new words file.")
        return new_words_counter

    def rewrite_new_words(self):
        """
        Rewrites the new
        """
        temp = self.new_words - self.WORDS
        with open(self.new_words_f, "w") as f:
            f.writelines("\n".join(temp.keys()))

    def prepare_model(self):
        """
        Makes a counter from hindi, english and newvocab file.
        """
        self.WORDS = self.spell_data_counter()
        self.WORDS = generic.filter_counter_n(self.WORDS)

        self.new_words = self.new_words_counter()
        self.rewrite_new_words()

        self.WORDS += self.new_words
        print(">> Prepared model")

    def save_counter(self):
        """
        Saves counter into a pickle file.
        """
        modelio.save_spell_model(self.WORDS)
        print(f">> Spelling correction model created at {self.model_f}.")
