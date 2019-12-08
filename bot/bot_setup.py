from pathlib import Path

from utils import db, fileio
from utils.generic import load_config


if __name__ == "__main__":
    config = load_config()
    assets_dir = Path(config["DIR"]["assets"])

    db_path = assets_dir / config["DB"]["file"]
    db.create_db(db_path)
    print(f"1. Created DB at {db_path}")

    db_config = config["DB"]
    db.create_db_tables(db_path, db_config)
    print("2. All tables created.")

    users_f = assets_dir / config["FILES"]["users_f"]
    fileio.create_file(users_f)
    msg = ("3. Empty users file created. "
           "This means everone (even strangers) will"
           "be allowed to use the commands")
    print(msg)

    start_f = assets_dir / config["FILES"]["start_f"]
    fileio.create_file(start_f)
    msg = ("4. Empty starters file created. "
           "Add more starter lines for the bot to use.")
    print(msg)

    key_val_f = assets_dir / config["FILES"]["key_val_f"]
    fileio.create_file(key_val_f)
    msg = ("5. Empty key-value pair JSON created. "
           "Add some key-value pairs you want the "
           "bot to fetch when you want it.")
    print(msg)
