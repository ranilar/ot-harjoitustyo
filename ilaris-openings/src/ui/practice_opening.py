import tkinter as tk, chess
from services.practice_service import PracticeService
from services.board_service import BoardService
from services.user_service import UserService


class PracticeOpening(tk.Frame):
    """
    A class to represent the practice opening frame in a Tkinter application.

    Args:
        PracticeService
        BoardService
        _show_choose_opening
        board_canvas
        comment_label

    Functions:
    update_board():
        Updates the board and comment label with the current state.
    next_move():
        Advances to the next move in the practice session.
    prev_move():
        Goes back to the previous move in the practice session.
    """
    def __init__(self, master, opening, _show_choose_opening):
        """
        Constructs all the necessary args for the PracticeOpening object.

        Args:
            master, tk.Tk or tk.Frame
            Opening
            _show_choose_opening
        """
        super().__init__(master)
        self.practice_service = PracticeService(opening)
        self.board_service = BoardService
        self._show_choose_opening = _show_choose_opening
        self._user_service = UserService()

        tk.Label(self, text=opening.name, font=("Garet", 20)).pack(pady=10)

        self.board_canvas = tk.Label(self)
        self.board_canvas.pack()

        self.comment_label = tk.Label(self, text="", font=("Garet", 14), wraplength=400)
        self.comment_label.pack(pady=10)

        self.move_entry = tk.Entry(self)
        self.quiz_mode = False

        self.check_move_button = tk.Button(self, text="Submit Move", command=self.check_move)        
        self.next_button = tk.Button(self, text="Next Move", command=self.next_move)
        self.prev_button = tk.Button(self, text="Previous Move", command=self.prev_move)
        self.prev_button.config(state="disabled")
        self.menu_button = tk.Button(self, text="Back To Openings", command=self._show_choose_opening)
        self.toggle_mode_button = tk.Button(self, text="Switch to Quiz Mode", command=self.toggle_mode)

        self.menu_button.pack(pady=10)        
        self.toggle_mode_button.pack(pady=10)
        self.next_button.pack(pady=10)
        self.prev_button.pack(pady=10)

        self.update_board()

    def update_board(self):
        """
        Updates the board, comment label and buttons with the current state.
        """
        if self.practice_service.move_index <= 0:
            self.prev_button.config(state="disabled")
        else:
            self.prev_button.config(state="normal")
            
        if self.practice_service.move_index >= len(self.practice_service.moves):
            self.next_button.config(state="disabled")
        else:
            self.next_button.config(state="normal")

        img = self.board_service.board_to_photoimage(self.practice_service.board)
        self.board_canvas.configure(image=img)
        self.board_canvas.image = img

        comment = self.practice_service.get_comment()
        self.comment_label.config(text=comment or "")

    def next_move(self):
        """
        Advances to the next move in the practice session, if there is one.
        """
        self.practice_service.next_move()
        self.update_board()

    def prev_move(self):
        """
        Goes back to the previous move in the practice session, if there is one.
        """
        self.practice_service.previous_move()
        self.update_board()

    def toggle_mode(self):
        """
        Handles switching between practice and quiz mode.
        """
        self.quiz_mode = not self.quiz_mode
        if self.quiz_mode:
            self.toggle_mode_button.config(text="Switch to Practice Mode")
            self.next_button.pack_forget()
            self.prev_button.pack_forget()
            self.move_entry.pack(pady=5)
            self.check_move_button.pack(pady=5)
            self.comment_label.config(text="Enter the next move in UCI format (e.g., e2e4):")
        else:
            self.toggle_mode_button.config(text="Switch to Quiz Mode")
            self.move_entry.pack_forget()
            self.check_move_button.pack_forget()
            self.next_button.pack(pady=10)
            self.prev_button.pack(pady=10)
            self.update_board()

    def check_move(self):
        """
        Handles move checking in quiz mode.
        """
        user_move = self.move_entry.get()
        expected_move = self.practice_service.get_expected_move()

        try:
            move_obj = chess.Move.from_uci(user_move)
            if move_obj == expected_move:
                self.practice_service.next_move()
                self.update_board()
                self.comment_label.config(text="Correct! Well done.")
            elif not expected_move:
                self.comment_label.config(text=f"No more moves!")
            else:
                self.comment_label.config(text=f"Incorrect! Try again.")
        except:
            self.comment_label.config(text="Invalid move format. Use UCI like 'e2e4'.")