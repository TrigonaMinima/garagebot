import json
import shutil
import unittest

from pathlib import Path

from context import fileio
from context import GenericCommandAPI as api


hard_repl = fileio.load_hard_replies()


class TestAPIFunctions(unittest.TestCase):
    """
    Tests all the API methods
    """

    def test_start(self):
        starters = fileio.load_starters() + [hard_repl["start"]["default"]]
        result = api.start()
        expected = starters
        self.assertIn(result, expected)

    def test_fetch_key_val(self):
        key_vals_orig = fileio.load_key_vals()

        for inp in ["", []]:
            result = api.fetch_key_val(inp)
            expected = json.dumps(key_vals_orig, indent=4)
            self.assertEqual(result, expected)

        for inp in ["1", ["1"]]:
            result = api.fetch_key_val(inp)
            expected = hard_repl["fetch"]["default"]
            self.assertEqual(result, expected)

        for key in key_vals_orig:
            result = api.fetch_key_val([key])
            expected = key_vals_orig[key]
            self.assertEqual(result, expected)

    def test_add_key_val(self):
        assets = Path(fileio.config["DIR"]["assets"])
        key_val_f = assets / fileio.config["FILES"]["key_val_f"]
        temp_key_val_f = assets / f"{key_val_f.stem}_temp{key_val_f.suffix}"
        shutil.copy(key_val_f, temp_key_val_f)

        for inp in ["", "2", [], ["2"], ["2", ','], [",", "2"]]:
            result = api.add_key_val(inp)
            expected = hard_repl["add_key_val"]["default_n"]
            self.assertEqual(result, expected)

        key_vals_orig = fileio.load_key_vals()

        inp = ["2", ",", "2"]
        result = api.add_key_val(inp)
        expected = hard_repl["add_key_val"]["default_y"]
        self.assertEqual(result, expected)

        result = fileio.load_key_vals()
        key_vals_orig["2"] = "2"
        expected = key_vals_orig
        self.assertDictEqual(result, expected)

        key_val_f.unlink()
        temp_key_val_f.rename(key_val_f)

    def test_pop_key_val(self):
        assets = Path(fileio.config["DIR"]["assets"])
        key_val_f = assets / fileio.config["FILES"]["key_val_f"]
        temp_key_val_f = assets / f"{key_val_f.stem}_temp{key_val_f.suffix}"
        shutil.copy(key_val_f, temp_key_val_f)

        # empty values
        for inp in ["", []]:
            result = api.pop_key_val(inp)
            expected = hard_repl["pop_key_val"]["default_n"]
            self.assertEqual(result, expected)

        # invalid values
        for inp in ["3", ["3"], ["3", ','], [",", "3"]]:
            key_vals_orig = fileio.load_key_vals()

            result = api.pop_key_val(inp)
            expected = hard_repl["pop_key_val"]["default_y"]
            self.assertEqual(result, expected)

            result = fileio.load_key_vals()
            expected = key_vals_orig
            self.assertDictEqual(result, expected)

        # valid values sent in a list
        key_vals_orig = fileio.load_key_vals()
        key_vals_temp = key_vals_orig.copy()
        for key in key_vals_orig:
            result = api.pop_key_val([key])
            expected = hard_repl["pop_key_val"]["default_y"]
            self.assertEqual(result, expected)

            result = fileio.load_key_vals()
            expected = key_vals_temp
            expected.pop(key)
            self.assertDictEqual(result, expected)

        key_val_f.unlink()
        temp_key_val_f.rename(key_val_f)

        # valid values sent as a string
        key_vals_orig = fileio.load_key_vals()
        for key in key_vals_orig:
            result = api.pop_key_val(key)
            expected = hard_repl["pop_key_val"]["default_y"]
            self.assertEqual(result, expected)

            result = fileio.load_key_vals()
            expected = key_vals_orig
            self.assertDictEqual(result, expected)

    def test_random_highlight(self):
        highlitghts = fileio.load_highlights() + ["Nothing to show"]
        self.assertIn(api.random_highlight(), highlitghts)

    def test_fuck_the_tables(self):
        replies = ["(╯ಠ_ಠ)╯︵ ┻━┻", "(╯°□°)╯︵ ┻━┻"]
        self.assertIn(api.fuck_the_tables(), replies)

    def test_respect_the_tables(self):
        self.assertEqual(api.respect_the_tables(), "┬─┬ノ(ಥ_ಥノ)")


if __name__ == '__main__':
    unittest.main()
