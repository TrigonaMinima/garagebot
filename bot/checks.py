from pathlib import Path

from exceptions import (ConfigDoesNotExist, DBDoesNotExist,
                        TableDoesNotExist, DirDoesNotExist)
from utils.db import generic
from utils.fileio import config


def check_config():
    config_path = Path("config.ini")
    if config_path.exists():
        return 1
    return 0


def check_model_file(file_path):
    if not file_path.exists():
        print()
        msg = (f"Model file ({file_path}) does not exist. "
               "Set it up using bot/bot_setup.py")
        raise FileNotFoundError(msg)
    else:
        print(f"> Model file ({file_path}) exists.")


def check_file(file_path):
    if not file_path.exists():
        print()
        msg = (f"{file_path} file does not exist. "
               "Set it up using bot/bot_setup.py")
        raise FileNotFoundError(msg)
    else:
        print(f"> {file_path} file exists.")


def check_dir(dir_path):
    if not dir_path.exists():
        msg = (f"{dir_path} directory does not exist. "
               "Set it up using bot/bot_setup.py")
        raise DirDoesNotExist(msg)
    else:
        print(f"> {dir_path} dir exists.")


def check():
    if not check_config():
        raise ConfigDoesNotExist

    assets_dir = Path(config["DIR"]["assets"])
    check_dir(assets_dir)

    models_dir = Path(config["DIR"]["models"])
    check_dir(models_dir)

    db_path = assets_dir / config["DB"]["file"]
    if not generic.check_db(db_path):
        msg = (f"Sqlite3 DB does not exist at {db_path}. "
               "Set it up using bot/bot_setup.py")
        raise DBDoesNotExist(msg)
    else:
        print("> Chat DB exists.")

    chat_table = config["DB"]["chat_table"]
    if not generic.check_table(db_path, chat_table):
        msg = (f"{chat_table} table does not exist. "
               "Set it up using bot/bot_setup.py")
        raise TableDoesNotExist(msg)
    else:
        print(f"> {chat_table} table exists.")

    users_f = assets_dir / config["FILES"]["users_f"]
    check_file(users_f)

    start_f = assets_dir / config["FILES"]["start_f"]
    check_file(start_f)

    key_val_f = assets_dir / config["FILES"]["key_val_f"]
    check_file(key_val_f)

    highlight_f = assets_dir / config["FILES"]["highlight_f"]
    check_file(highlight_f)

    hard_repl_f = assets_dir / config["FILES"]["hard_repl_f"]
    check_file(hard_repl_f)

    pos_rep_f = assets_dir / config["FILES"]["pos_rep_f"]
    check_file(pos_rep_f)

    neg_rep_f = assets_dir / config["FILES"]["neg_rep_f"]
    check_file(neg_rep_f)

    singular_cuss_f = assets_dir / config["FILES"]["singular_cuss_f"]
    check_file(singular_cuss_f)

    bot_alias_f = assets_dir / config["META"]["bot_alias_f"]
    check_file(bot_alias_f)

    cuss_all_f = assets_dir / config["FILES"]["cuss_all_f"]
    check_file(cuss_all_f)

    spell_model_f = models_dir / config["MODEL"]["spell_f"]
    check_model_file(spell_model_f)

    data_dir = Path(config["DIR"]["data"])
    spell_correct_f = data_dir / config["DATA"]["spell_correct_f"]
    check_file(spell_correct_f)

    spell_wrong_f = data_dir / config["DATA"]["spell_wrong_f"]
    check_file(spell_wrong_f)

    spell_new_f = data_dir / config["DATA"]["spell_new_f"]
    check_file(spell_new_f)

    stop_hing_f = assets_dir / config["FILES"]["stop_hing_f"]
    check_file(stop_hing_f)

    return 1


if __name__ == "__main__":
    check()
