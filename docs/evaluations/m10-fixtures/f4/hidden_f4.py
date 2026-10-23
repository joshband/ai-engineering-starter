import unittest
from cachekit.config import load_config

class Hidden(unittest.TestCase):
    def test_comments_and_hash_rules(self):
        self.assertEqual(load_config("# c\n  # c2\na = 1"), {"a": "1"})
        self.assertEqual(load_config("a = 1 # note"), {"a": "1"})
        self.assertEqual(load_config("a=b#c"), {"a": "b#c"})
        self.assertEqual(load_config("a = b #c"), {"a": "b"})
        self.assertEqual(load_config("a=b#c #d"), {"a": "b#c"})
        self.assertEqual(load_config("a = 1# no"), {"a": "1# no"})
    def test_quoted(self):
        self.assertEqual(load_config('a = "x y"'), {"a": "x y"})
        self.assertEqual(load_config('a = "x # y"'), {"a": "x # y"})
        self.assertEqual(load_config('a = "k=v"'), {"a": "k=v"})
        self.assertEqual(load_config('a = "q\\"uote"'), {"a": 'q"uote'})
        self.assertEqual(load_config('a = "back\\\\slash"'), {"a": "back\\slash"})
        self.assertEqual(load_config('a = ""'), {"a": ""})
        self.assertEqual(load_config('a = "x" # note'), {"a": "x"})
        self.assertEqual(load_config('a="x"   # note'), {"a": "x"})
        self.assertEqual(load_config('a = "  padded  "'), {"a": "  padded  "})
    def test_quoted_errors(self):
        for bad in ['a = "x" y', 'a = "x', 'a = "bad\\n"', 'a = "x"# note', 'a = "x""y"', 'a = "x\\']:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    load_config(bad)
    def test_duplicates_unchanged(self):
        self.assertEqual(load_config("a=1\na=2"), {"a": "2"})
    def test_old_errors(self):
        for bad in ["not a pair", "1a = x", "=v"]:
            with self.assertRaises(ValueError):
                load_config(bad)

if __name__ == "__main__":
    unittest.main()
