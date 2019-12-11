import json
import configparser

from pathlib import Path


def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


def create_file(file_path):
    if not file_path.exists():
        f = open(file_path, "w")
        f.close()


def load_file(file_path):
    if not file_path.exists():
        return []

    with open(file_path, "r") as f:
        lines = [i.strip() for i in f if i]
    return lines


def dump_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)


def load_json(file_path):
    if not file_path.exists():
        return {}

    with open(file_path, "r") as f:
        data = json.loads(f.read())
    return data


def dump_json(file_path, data):
    data = json.dumps(data, indent=4)
    with open(file_path, "w") as f:
        f.write(data)


def load_starters():
    assets_dir = Path(config["DIR"]["assets"])
    starters_file = assets_dir / config["FILES"]["start_f"]
    starters = load_file(starters_file)
    return starters


def load_users():
    assets_dir = Path(config["DIR"]["assets"])
    users_file = assets_dir / config["FILES"]["users_f"]
    users = load_file(users_file)
    return users


def load_highlights():
    assets_dir = Path(config["DIR"]["assets"])
    highlight_f = assets_dir / config["FILES"]["highlight_f"]
    highlights = load_file(highlight_f)
    return highlights


def load_key_vals():
    assets_dir = Path(config["DIR"]["assets"])
    key_val_file = assets_dir / config["FILES"]["key_val_f"]
    key_vals = load_json(key_val_file)
    return key_vals


def dump_key_vals(data):
    assets_dir = Path(config["DIR"]["assets"])
    key_val_file = assets_dir / config["FILES"]["key_val_f"]
    dump_json(key_val_file, data)


def load_hard_replies():
    assets_dir = Path(config["DIR"]["assets"])
    hard_repl_f = assets_dir / config["FILES"]["hard_repl_f"]
    hard_repl = load_json(hard_repl_f)
    return hard_repl


def load_pos_rep():
    assets_dir = Path(config["DIR"]["assets"])
    pos_rep_f = assets_dir / config["FILES"]["pos_rep_f"]
    pos_rep = load_file(pos_rep_f)
    return pos_rep


def load_neg_rep():
    assets_dir = Path(config["DIR"]["assets"])
    neg_rep_f = assets_dir / config["FILES"]["neg_rep_f"]
    neg_rep = load_file(neg_rep_f)
    return neg_rep


def load_singular_cusses():
    assets_dir = Path(config["DIR"]["assets"])
    singular_cuss_f = assets_dir / config["FILES"]["singular_cuss_f"]
    cusses = load_file(singular_cuss_f)
    return cusses


def load_all_cusses():
    assets_dir = Path(config["DIR"]["assets"])
    cuss_all_f = assets_dir / config["FILES"]["cuss_all_f"]
    cusses = load_file(cuss_all_f)
    return cusses


def load_bot_alias():
    assets_dir = Path(config["DIR"]["assets"])
    bot_alias_f = assets_dir / config["META"]["bot_alias_f"]
    aliases = load_file(bot_alias_f)
    return set(aliases)


config = load_config()
