from pathlib import Path

from utils import fileio
from utils.db import generic
from utils.fileio import config
from intel.spell_train import StatSpellCorrectorTrain


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
    },
    "yt": {
        "default_n1": "Cant watch a video that big!!",
        "default_n2": "That video is too small to make any sense of!!",
        "default_y": "Interesting vid. Anybody else done watching this video?"
    },
    "vulgar": {
        "default_n": "No one is vulgar right now."
    },
    "weekly_cussing": {
        "default_y1": "Starting new week! Scores from the previous week:\n\n",
        "default_y2": "\nPlease don't cuss as much this week.",
        "default_n": "Great work! No one cussed this week!"
    },
    "weekly_commands": {
        "default_y": "Command stats:\n\n",
        "default_n": "No one used any commands last week. :("
    },
    "weekly_quotes": {
        "default_y": "Quote stats:\n\n",
        "default_n": "No one quoted anyone last week. :("
    }
}

default_singular_cuss = ["F**k"]

if __name__ == "__main__":
    assets_dir = Path(config["DIR"]["assets"])
    assets_dir.mkdir(exist_ok=True)
    print(f"> Created assets dir ({assets_dir})")

    models_dir = Path(config["DIR"]["models"])
    models_dir.mkdir(exist_ok=True)
    (models_dir / "spell").mkdir(exist_ok=True)
    print(f"> Created models dir ({models_dir})")

    data_dir = Path(config["DIR"]["data"])
    data_dir.mkdir(exist_ok=True)
    (data_dir / "spell").mkdir(exist_ok=True)
    print(f"> Created data dir ({data_dir})")

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

    singular_cuss_f = assets_dir / config["FILES"]["singular_cuss_f"]
    fileio.create_file(singular_cuss_f)
    default_singular_cuss = "\n".join(default_singular_cuss)
    if singular_cuss_f.stat().st_size == 0:
        fileio.dump_file(singular_cuss_f, default_singular_cuss)
    msg = (f"> Default cuss file ({singular_cuss_f}) created. "
           "Update the file as needed")
    print(msg)

    bot_alias_f = assets_dir / config["META"]["bot_alias_f"]
    fileio.create_file(bot_alias_f)
    msg = (f"> Empty bot alias file ({bot_alias_f}) created. "
           "Add the bot aliases as needed")
    print(msg)

    cuss_all_f = assets_dir / config["FILES"]["cuss_all_f"]
    fileio.create_file(cuss_all_f)
    msg = (f"> Empty cusses file ({cuss_all_f}) created. "
           "Select your naughty strings from here - "
           "https://github.com/minimaxir/big-list-of-naughty-strings")
    print(msg)

    model_train_f = data_dir / config["DATA"]["spell_data_f"]
    model_f = models_dir / config["MODEL"]["spell_f"]
    if model_train_f.exists():
        print("> Training spelling correction model.")
        StatSpellCorrectorTrain()
    elif model_f.exists():
        print(f"> No training file ({model_train_f}) exists. "
              f"Previous model file ({model_f}) exists. Will use that. To "
              "update it add the training data and run bot/bot_setup.py again.")
    else:
        msg = ("Spelling correction training file does not exist."
               "Older model also doesn't exist."
               f"Add a training file at {model_train_f} to continue.")
        raise FileNotFoundError(msg)

    data_dir.mkdir(exist_ok=True)
    (data_dir / "spell").mkdir(exist_ok=True)
    print(f"> Created data dir ({data_dir})")

    spell_correct_f = data_dir / config["DATA"]["spell_correct_f"]
    fileio.create_file(spell_correct_f)
    msg = (f"> Empty spell correction related file ({spell_correct_f}) "
           "created.")
    print(msg)

    spell_wrong_f = data_dir / config["DATA"]["spell_wrong_f"]
    fileio.create_file(spell_wrong_f)
    msg = (f"> Empty spell correction related file ({spell_wrong_f}) "
           "created.")
    print(msg)

    spell_new_f = data_dir / config["DATA"]["spell_new_f"]
    fileio.create_file(spell_new_f)
    msg = (f"> Empty spell correction related file ({spell_new_f}) "
           "created.")
    print(msg)

    stop_hing_f = assets_dir / config["FILES"]["stop_hing_f"]
    fileio.create_file(stop_hing_f)
    msg = (f"> Empty hinglish stop words file ({stop_hing_f}) created. "
           "Update the file with stop words to be removed from the wordcloud "
           "as needed")
    print(msg)
