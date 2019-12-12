import os
import sys

mod_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')) + "/bot"
sys.path.insert(0, mod_path)


from utils import fileio
from api.generic import GenericCommandAPI
from utils import text as text_utils
