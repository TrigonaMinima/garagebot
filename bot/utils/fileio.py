from pathlib import Path

from utils.generic import load_config


config = load_config()


def create_file(file_path):
    if not file_path.exists():
        f = open(file_path, "w")
        f.close()


def load_file(file_path):
    lines = [i.strip() for i in open(file_path, "r") if i]
    return lines


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
