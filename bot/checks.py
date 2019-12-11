from pathlib import Path

from exceptions import ConfigDoesNotExistError, DBDoesNotExistError, TableDoesNotExist
from utils.db import generic
from utils.fileio import config


def check_config():
    config_path = Path("config.ini")
    if config_path.exists():
        return 1
    return 0


def check_file(file_path):
    if not file_path.exists():
        print()
        msg = (f"{file_path} file does not exist. "
               "Set it up using bot/bot_setup.py")
        raise FileNotFoundError(msg)
    else:
        print(f"> {file_path} file exists.")


def check():
    if not check_config():
        raise ConfigDoesNotExistError

    assets_dir = Path(config["DIR"]["assets"])

    db_path = assets_dir / config["DB"]["file"]
    if not generic.check_db(db_path):
        msg = (f"Sqlite3 DB does not exist at {db_path}. "
               "Set it up using bot/bot_setup.py")
        raise DBDoesNotExistError(msg)
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

    return 1


if __name__ == "__main__":
    check()
