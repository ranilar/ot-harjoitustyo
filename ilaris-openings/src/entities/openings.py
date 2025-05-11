class Opening:
    def __init__(self, name, game, comments):
        self.name = name
        self.game = game
        self.comments = comments

    def get_comment(self, move_index):
        return self.comments.get(move_index)
