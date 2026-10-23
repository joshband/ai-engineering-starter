import unittest
from cachekit.sizes import parse_size

class Hidden(unittest.TestCase):
    def test_decimals(self):
        self.assertEqual(parse_size("1.5MB"), 1572864)
        self.assertEqual(parse_size("0.5kb"), 512)
        self.assertEqual(parse_size("0.3KB"), 307)
    def test_spaces(self):
        self.assertEqual(parse_size("1.5 MB"), 1572864)
        self.assertEqual(parse_size("2   gb"), 2 * 1024 ** 3)
        self.assertEqual(parse_size("  7 KB  "), 7168)
    def test_still_ints(self):
        self.assertEqual(parse_size("10KB"), 10240)
    def test_rejects(self):
        for bad in [".5KB", "5.KB", "-1KB", "+1KB", "1e3KB", "1_000KB", "1..5KB", "1.5.2KB", "1\tKB", "1\nKB", "KB", "1 TB", "", "1.5"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parse_size(bad)
    def test_returns_int(self):
        self.assertIsInstance(parse_size("1.5KB"), int)

if __name__ == "__main__":
    unittest.main()
