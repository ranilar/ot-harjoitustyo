import tkinter as tk
from PIL import Image, ImageTk
import os

class Menu(tk.Frame):
    """
    The main menu UI for the Chess Opening Trainer.
    Displays a background image and a button to start training.
    """

    def __init__(self, master, choose_opening):
        """
        Initializes the Menu frame.

        Args:
            The parent Tkinter container.
            Function to call when 'Start Training' is clicked.
        """
        super().__init__(master)

        self._choose_opening = choose_opening

        WINDOW_WIDTH = 743
        WINDOW_HEIGHT = 745
        master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        current_dir = os.path.dirname(__file__)
        image_path = os.path.abspath(os.path.join(current_dir, "..", "assets", "blurred_board.png"))

        bg_image = Image.open(image_path)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        canvas.create_text(400, 100, text="Chess Opening Trainer", font=("Garet", 32), fill="black")

        start_btn = tk.Button(self, text="Start Training", font=("Garet", 16), command=self._choose_opening)
        canvas.create_window(400, 300, window=start_btn)
