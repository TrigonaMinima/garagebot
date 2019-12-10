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
    with open(file_path, "r") as f:
        lines = [i.strip() for i in f if i]
    return lines


def load_json(file_path):
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


config = load_config()
