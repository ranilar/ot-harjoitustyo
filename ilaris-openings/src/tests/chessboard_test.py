import unittest
import tkinter as tk
from ui.main_menu import Menu

class TestChessView(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = Menu