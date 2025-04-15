from openings import openings

def get_opening(name):
    return openings.get(name)

def check_user_move(opening, user_move, move_index):
    expected_move = opening.get_move(move_index)
    return user_move == expected_move
