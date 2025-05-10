import tkinter as tk
import os
from services.board_service import BoardService

class ChooseOpening(tk.Frame):
    """
    UI view for selecting a chess opening to practice. 
    Displays available PGN files as selectable buttons.
    """

    def __init__(self, master, switch_to_practice_view, show_main_menu):
        """
        Initialize the ChooseOpening view.

        Args:
            The parent Tkinter container.
            Function to call when an opening is selected.
        """
        super().__init__(master)
        self.switch_to_practice_view = switch_to_practice_view
        self.show_main_menu = show_main_menu
        self.board_service = BoardService
        
        self._initialize()

    def _initialize_widgets(self):
            tk.Label(self, text="Choose an Opening", font=("Garet", 24)).pack(pady=10)
            tk.Button(self, text="Go Back", font=("Garet", 17), command=self.show_main_menu).pack(pady=20)

            files = [f for f in os.listdir("src/openings") if f.endswith(".pgn")]

            for file in files:
                display_name = file.replace(".pgn", "").replace("_", " ").title()
                tk.Button(self, text=display_name, font=("Garet", 16),
                        command=lambda f=file: self._select_opening(f)).pack(pady=5)            

    def _select_opening(self, file_name):
        """
        Loads the selected opening and switches to the practice view.

        Args:
            The filename of the selected PGN file.
        """
        opening = self.board_service.load_opening_from_pgn(os.path.join("src", "openings", file_name))
        self.switch_to_practice_view(opening)

    def _initialize(self):
        self._initialize_widgets()