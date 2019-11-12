import random

team_name = 'E5'
strategy_name = 'Collude first 100 rounds unless betrayed. Betray 101st round forward.'
strategy_description = '''\
Betray if ever betrayed.
If I haven't been betrayed yet, I'll betray starting with the 100th round.
'''

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

    # If the other player has betrayed or this is the last half of the game,
    if their_last_move == 'b' or num_rounds > 100:
        return 'b'               # Betray.
    else:
        return 'c'         # but 90% of the time collude
