from pathlib import Path

from utils.generic import load_config


def create_file(file_path):
    if not file_path.exists():
        f = open(file_path, "w")
        f.close()


def load_starters():
    config = load_config()
    assets_dir = Path(config["DIR"]["assets"])
    starters_file = assets_dir / config["FILES"]["start_f"]
    starters = [i.strip() for i in open(starters_file, "r") if i]
    return starters
