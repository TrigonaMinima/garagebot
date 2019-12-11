from pathlib import Path

from utils import fileio
from utils.db import generic
from utils.fileio import config


hard_repl = {
    "start": {
        "default": "Hi!"
    },
    "fetch": {
        "default": "Provide the right argument bro!"
    },
    "add_key_val": {
        "default_y": "Added to the list!",
        "default_n": "Provide the right argument bro!"
    },
    "pop_key_val": {
        "default_y": "Removed from the list!",
        "default_n": "Nothing to remove!"
    },
    "random_highlight": {
        "default": "Nothing to show!"
    },
    "scream": {
        "default": ", dont scream plez"
    }
}

if __name__ == "__main__":
    assets_dir = Path(config["DIR"]["assets"])

    db_path = assets_dir / config["DB"]["file"]
    generic.create_db(db_path)
    print(f"> Created DB at {db_path}")

    db_config = config["DB"]
    generic.create_db_tables(db_path, db_config)
    print("> All tables created.")

    users_f = assets_dir / config["FILES"]["users_f"]
    fileio.create_file(users_f)
    msg = (f"> Empty users file ({users_f}) created. "
           "This means everyone (even strangers) will "
           "be allowed to use the commands")
    print(msg)

    start_f = assets_dir / config["FILES"]["start_f"]
    fileio.create_file(start_f)
    msg = (f"> Empty starters file ({start_f}) created. "
           "Add more starter lines for the bot to use.")
    print(msg)

    key_val_f = assets_dir / config["FILES"]["key_val_f"]
    fileio.create_file(key_val_f)
    msg = (f"> Empty key-value pair JSON ({key_val_f}) created. "
           "Add some key-value pairs you want the "
           "bot to fetch when you want it.")
    print(msg)

    highlight_f = assets_dir / config["FILES"]["highlight_f"]
    fileio.create_file(highlight_f)
    msg = (f"> Empty highlights file ({highlight_f}) created. "
           "Add some awesome dialogues or sayings or group memories for "
           "the bot.")
    print(msg)

    hard_repl_f = assets_dir / config["FILES"]["hard_repl_f"]
    fileio.create_file(hard_repl_f)
    if hard_repl_f.stat().st_size == 0:
        fileio.dump_json(hard_repl_f, hard_repl)
    msg = (f"> Default hard replies file ({hard_repl_f}) created. "
           "Update the default replies for each command as needed")
    print(msg)

    pos_rep_f = assets_dir / config["FILES"]["pos_rep_f"]
    fileio.create_file(pos_rep_f)
    msg = (f"> Default positive replies file ({pos_rep_f}) created. "
           "Update the default replies as needed.")
    print(msg)

    neg_rep_f = assets_dir / config["FILES"]["neg_rep_f"]
    fileio.create_file(neg_rep_f)
    msg = (f"> Default negative replies file ({neg_rep_f}) created. "
           "Update the default replies as needed")
    print(msg)
