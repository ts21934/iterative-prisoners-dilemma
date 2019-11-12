team_name = 'E2'
strategy_name = 'Alternate'
strategy_description = 'Collude, then alternate.'

num_rounds = -1

def move(my_last_move, their_last_move):
    '''
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    '''
    global num_rounds
    num_rounds += 1

    # This player colludes on even numbered rounds (first round is round #0).
    if num_rounds % 2 == 0:
        return 'c'
    else:
        return 'b'
