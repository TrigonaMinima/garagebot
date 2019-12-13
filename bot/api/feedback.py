from pathlib import Path

from utils import fileio
from api.monitor import corrector


class FeedbackHandlerAPI(object):
    @staticmethod
    def correction_feedback(option, correction):
        data_dir = Path(fileio.config["DIR"]["data"])
        spell_correct_f = data_dir / fileio.config["FEED"]["spell_correct_f"]
        spell_wrong_f = data_dir / fileio.config["FEED"]["spell_wrong_f"]
        spell_new_f = data_dir / fileio.config["FEED"]["spell_new_f"]

        flag = 0
        option = option.split("_")[0]
        correction = correction.split("/")
        if option[0] == "1":
            flag = 1
            case = f"{correction[1]},{correction[2]}\n"
            fileio.append_file(spell_correct_f, case)
        elif option[0] == "0":
            flag = 0
            new_word = [correction[1]]
            corrector.update(new_word)

            case = "\n".join(new_word) + "\n"
            fileio.append_file(spell_new_f, case)
        elif option[0] == "2":
            flag = 2
            case = f"{correction[1]},{correction[2]}\n"
            fileio.append_file(spell_wrong_f, case)
        return flag
