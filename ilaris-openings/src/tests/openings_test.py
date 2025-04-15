import unittest
import os
from openings.openings import Opening

class TestOpening(unittest.TestCase):
    def setUp(self):
        self.sample_pgn_path = os.path.join(os.path.dirname(__file__), "test.pgn")
        with open(self.sample_pgn_path, "w") as f:
            f.write("""
[Event "?"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "You"]
[Black "Opponent"]
[Result "*"]
[Opening "Queen's Gambit"]

1. d4 {A strong center} d5 {Initiates gambit} 2. c4 *

""")

    def test_loading_opening(self):
        opening = Opening.load_opening_from_pgn(self.sample_pgn_path)
        self.assertEqual(opening.name, "Queen's Gambit")
        print(opening.get_comment(0))
        self.assertEqual(opening.get_comment(0), "A strong center")
        self.assertEqual(opening.get_comment(1), "Initiates gambit")

    def tearDown(self):
        os.remove(self.sample_pgn_path)

if __name__ == '__main__':
    unittest.main()
