from pathlib import Path

from exceptions import DBDoesNotExistError, TableDoesNotExist
from utils import db
from utils.generic import load_config


config = load_config()


def check():
    assets_dir = Path(config["DIR"]["assets"])

    db_path = assets_dir / config["DB"]["file"]
    if not db.check_db(db_path):
        msg = (f"Sqlite3 DB does not exist at {db_path}. "
               "Set it up using bot/bot_setup.py")
        raise DBDoesNotExistError(msg)
    else:
        print("1. Chat DB exists.")

    chat_table = config["DB"]["chat_table"]
    if not db.check_table(db_path, chat_table):
        msg = (f"{chat_table} table does not exist. "
               "Set it up using bot/bot_setup.py")
        raise TableDoesNotExist(msg)
    else:
        print(f"2. {chat_table} table exists.")

    users_f = assets_dir / config["FILES"]["users_f"]
    if not users_f.exists():
        msg = (f"{users_f} file does not exist. "
               "Set it up using bot/bot_setup.py")
        raise FileNotFoundError(msg)
    else:
        print(f"3. {users_f} file exists.")

    start_f = assets_dir / config["FILES"]["start_f"]
    if not start_f.exists():
        msg = (f"{start_f} file does not exist in {assets_dir}. "
               "Set it up using bot/bot_setup.py")
        raise FileNotFoundError(msg)
    else:
        print(f"4. {start_f} file exists.")

    return 1


if __name__ == "__main__":
    check()
