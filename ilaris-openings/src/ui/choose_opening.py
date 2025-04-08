import tkinter as tk

class ChooseOpening(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Choose an Opening", font=("Garet", 24)).pack(pady=20)

        openings = ["Sicilian Defense", "Queen's Gambit"]

        for opening in openings:
            tk.Button(self, text=opening, font=("Garet", 16), command=lambda o=opening: self._select_opening(o)).pack(pady=5)

    def _select_opening(self, opening_name):
        print(f"Selected: {opening_name}")