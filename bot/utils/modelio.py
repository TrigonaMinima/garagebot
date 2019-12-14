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


def save_pickle(file_path, data):
    with open(file_path, 'wb') as w:
        pickle.dump(data, w)


def load_spell_model():
    """
    Loads a spelling correction model and returns the binary object.
    """
    models_dir = Path(config["DIR"]["models"])
    spell_f = models_dir / config["MODEL"]["spell_f"]
    model = load_pickle_dump(spell_f)
    return model


def save_spell_model(model):
    """
    Receives a spelling correction model and saves it at the
    appropriate location according to config
    """
    models_dir = Path(config["DIR"]["models"])
    spell_f = models_dir / config["MODEL"]["spell_f"]
    save_pickle(spell_f, model)
