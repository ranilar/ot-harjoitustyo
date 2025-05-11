import chess

class PracticeService:
    """
    Service class for handling the logic of practicing a chess opening.
    Manages move navigation and comment retrieval for a given opening.
    """

    def __init__(self, opening):
        """
        Initializes the PracticeService with an opening.

        Args:
            The opening to practice, containing a game and comments.
        """
        self.opening = opening
        self.moves = list(opening.game.mainline_moves())
        self.move_index = 0
        self.board = chess.Board()
        self.quiz_mode = False

    def next_move(self):
        """
        Advances the board state by one move, if more moves are available.
        """
        if self.move_index < len(self.moves):
            move = self.moves[self.move_index]
            self.board.push(move)
            self.move_index += 1

    def previous_move(self):
        """
        Reverts the board state by one move, if any moves have been made.
        """
        if self.move_index > 0:
            self.move_index -= 1
            self.board.pop()

    def get_comment(self):
        """
        Retrieves the comment associated with the current move, if available.

        Returns:
            str or None: The comment for the most recent move, or None if none exists.
        """
        if self.move_index == 0:
            return None
        return self.opening.get_comment(self.move_index - 1)

    def get_expected_move(self):
        if self.move_index < len(self.moves):
            return self.moves[self.move_index]
        return None
