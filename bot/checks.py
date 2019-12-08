from pathlib import Path

from exceptions import DBDoesNotExistError, TableDoesNotExist
from utils import db
from utils.generic import load_config


config = load_config()


def check_file(file_path):
    if not file_path.exists():
        print()
        msg = (f"{file_path} file does not exist. "
               "Set it up using bot/bot_setup.py")
        raise FileNotFoundError(msg)
    else:
        print(f"> {file_path} file exists.")


def check():
    assets_dir = Path(config["DIR"]["assets"])

    db_path = assets_dir / config["DB"]["file"]
    if not db.check_db(db_path):
        msg = (f"Sqlite3 DB does not exist at {db_path}. "
               "Set it up using bot/bot_setup.py")
        raise DBDoesNotExistError(msg)
    else:
        print("> Chat DB exists.")

    chat_table = config["DB"]["chat_table"]
    if not db.check_table(db_path, chat_table):
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

    return 1


if __name__ == "__main__":
    check()
