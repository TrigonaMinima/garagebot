import json
import random

from pathlib import Path

from utils import fileio


hard_repl = fileio.load_hard_replies()


class GenericCommandAPI(object):
    """
    Class containing static methods of generic commands.
    """

    @staticmethod
    def start():
        """
        Method for the "/start" command
        """
        starter = hard_repl["start"]["default"]
        starters = fileio.load_starters()
        if starters:
            starter = random.choice(starters)
        return starter

    @staticmethod
    def fetch_key_val(argument: list):
        """
        Method for the "/fetch" command
        """
        key_val_dict = fileio.load_key_vals()

        argument = " ".join(argument).strip()
        if argument:
            default_reply = hard_repl["fetch"]["default"]
            val = key_val_dict.get(argument, default_reply)
        else:
            val = json.dumps(key_val_dict, indent=4)
        return val

    @staticmethod
    def add_key_val(argument: list):
        """
        Method for the "/add" command
        """
        key_val_dict = fileio.load_key_vals()

        argument = [i.strip() for i in " ".join(argument).strip().split(",")]
        if len(argument) == 2 and argument[0] and argument[1]:
            reply = hard_repl["add_key_val"]["default_y"]
            key_val_dict[argument[0]] = argument[1]
            fileio.dump_key_vals(key_val_dict)
        else:
            reply = hard_repl["add_key_val"]["default_n"]

        return reply

    @staticmethod
    def pop_key_val(argument: list):
        """
        Method for the "/pop" command
        """
        key_val_dict = fileio.load_key_vals()

        argument = " ".join(argument).strip()
        if argument:
            reply = hard_repl["pop_key_val"]["default_y"]
            _ = key_val_dict.pop(argument, None)
            fileio.dump_key_vals(key_val_dict)
        else:
            reply = hard_repl["pop_key_val"]["default_n"]

        return reply

    @staticmethod
    def random_highlight():
        """
        Returns a random highlight from the highlights file.
        TODO: generalise the hard coded reply
        """
        highlights = fileio.load_highlights()
        if highlights:
            highlight = random.choice(highlights)
        else:
            highlight = hard_repl["random_highlight"]["default"]
        return highlight

    @staticmethod
    def fuck_the_tables():
        """
        Copied from the fuckthetables bot on Reddit.
        """
        string = random.choice(["(╯ಠ_ಠ)╯︵ ┻━┻", "(╯°□°)╯︵ ┻━┻"])
        return string

    @staticmethod
    def respect_the_tables():
        """
        Opposite of the fuckthetables bot. This one respects the tables.
        """
        string = "┬─┬ノ(ಥ_ಥノ)"
        return string
