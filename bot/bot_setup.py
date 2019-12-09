from pathlib import Path

from utils import fileio
from utils.db import generic
from utils.generic import load_config


if __name__ == "__main__":
    config = load_config()
    assets_dir = Path(config["DIR"]["assets"])

    db_path = assets_dir / config["DB"]["file"]
    generic.create_db(db_path)
    print(f"> Created DB at {db_path}")

    db_config = config["DB"]
    generic.create_db_tables(db_path, db_config)
    print("> All tables created.")

    users_f = assets_dir / config["FILES"]["users_f"]
    fileio.create_file(users_f)
    msg = ("> Empty users file created. "
           "This means everone (even strangers) will "
           "be allowed to use the commands")
    print(msg)

    start_f = assets_dir / config["FILES"]["start_f"]
    fileio.create_file(start_f)
    msg = ("> Empty starters file created. "
           "Add more starter lines for the bot to use.")
    print(msg)

    key_val_f = assets_dir / config["FILES"]["key_val_f"]
    fileio.create_file(key_val_f)
    msg = ("> Empty key-value pair JSON created. "
           "Add some key-value pairs you want the "
           "bot to fetch when you want it.")
    print(msg)

    highlight_f = assets_dir / config["FILES"]["highlight_f"]
    fileio.create_file(highlight_f)
    msg = ("> Empty highlights file created. "
           "Add some awesome dialogues or sayings or group memories for"
           "the bot to give them to you at random.")
    print(msg)
