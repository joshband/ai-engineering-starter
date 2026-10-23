import unittest
from cachekit.duration import parse_duration

class Hidden(unittest.TestCase):
    def test_valid(self):
        cases = {"1h30m": 5400, "90s": 90, "1h 30m": 5400, "2m5s": 125, "1h2m3s": 3723, "01h": 3600,
                 "0s": 0, " 45m ": 2700, "2h5s": 7205, "1h 2m 3s": 3723, "10m 5s": 605, "000s": 0}
        for text, want in cases.items():
            with self.subTest(text=text):
                self.assertEqual(parse_duration(text), want)
    def test_returns_int(self):
        self.assertIsInstance(parse_duration("1h30m"), int)
    def test_invalid(self):
        bad = ["30m1h", "1h1h", "5s1m", "10", "1H", "1ms", "1 h", "1h  30m", "", "   ", "-5s", "+5s",
               "1.5h", "1_0s", "1h30", "h", "1h-30m", "1h\n30m", "1h\t30m", "１h", "1m1m", "1h30m1h",
               "1h 30m x", "1hh", "1m 5", "1d"]
        for text in bad:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_duration(text)

if __name__ == "__main__":
    unittest.main()
