import unittest
import chess # type: ignore
import tkinter as tk
from PIL import ImageTk
from index import ChessView

class TestChessView(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = ChessView(self.root)

    def test_board_init(self):
        wanted_configuration = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        
        self.assertEqual(self.app.board.fen(), wanted_configuration)