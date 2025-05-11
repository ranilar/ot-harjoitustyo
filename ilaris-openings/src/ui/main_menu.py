import tkinter as tk
from PIL import Image, ImageTk
import os

class Menu(tk.Frame):
    """
    The main menu UI for the Chess Opening Trainer.
    Displays a background image and a button to start training.
    """

    def __init__(self, master, choose_opening, login_page):
        """
        Initializes the Menu frame.

        Args:
            The parent Tkinter container.
            Function to call when 'Start Training' is clicked.
        
        Functions:
            _inititalize_window(): Creates the window with all its' widgets
            _initialize(): Initializes the Menu UI
        """
        super().__init__(master)

        self._choose_opening = choose_opening
        self._login_page = login_page
        self.master = master

        self._initialize()

    def _initialize_window(self):
            WINDOW_WIDTH = 743
            WINDOW_HEIGHT = 745
            self.master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

            current_dir = os.path.dirname(__file__)
            image_path = os.path.abspath(os.path.join(current_dir, "..", "assets", "blurred_board.png"))

            bg_image = Image.open(image_path)
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
            canvas.pack(fill="both", expand=True)

            canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
            canvas.create_text(400, 100, text="Chess Opening Trainer", font=("Garet", 32), fill="black")
            
            start_btn = tk.Button(self, text="Start Training", font=("Garet", 16), command=self._choose_opening, padx=5, pady=5)
            user_label = tk.Label(self, text=f"Logged in as: test", font=("Garet", 14))
            logout_btn = tk.Button(self, text="Log out", font=("Garet", 16), command=self._user_service.logout, padx=5, pady=5)
            canvas.create_window(400, 250, window=start_btn)
            canvas.create_window(620, 20, window=user_label)
            canvas.create_window(400, 350, window=logout_btn)
        
    def _initialize(self):
        self._initialize_window()