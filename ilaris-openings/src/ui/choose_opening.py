import tkinter as tk
import os
from openings.openings import Opening
from ui.practice_opening import PracticeOpening

class ChooseOpening(tk.Frame):
    def __init__(self, master, switch_to_practice_view):
        super().__init__(master)
        self.switch_to_practice_view = switch_to_practice_view

        tk.Label(self, text="Choose an Opening", font=("Garet", 24)).pack(pady=20)

        files = [f for f in os.listdir("src/openings") if f.endswith(".pgn")]

        for file in files:
            display_name = file.replace(".pgn", "").replace("_", " ").title()
            tk.Button(self, text=display_name, font=("Garet", 16),
                      command=lambda f=file: self._select_opening(f)).pack(pady=5)

    def _select_opening(self, file_name):
        opening = Opening.load_opening_from_pgn(os.path.join("src", "openings", file_name))
        self.switch_to_practice_view(opening)