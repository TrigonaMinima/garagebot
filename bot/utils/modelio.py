import pickle

from pathlib import Path

from utils import fileio


config = fileio.config


def load_pickle_dump(file_path):
    if not file_path.exists():
        return None

    with open(file_path, "rb") as f:
        bin_data = pickle.load(f)
    return bin_data


def load_spell_model():
    models_dir = Path(config["DIR"]["models"])
    spell_f = models_dir / config["MODEL"]["spell_f"]
    model = load_pickle_dump(spell_f)
    return model
