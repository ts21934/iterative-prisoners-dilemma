team_name = 'E3'
strategy_name = 'Collude but retaliate'
strategy_description = '''\
Collude first round. Collude, except in a round after getting
a severe punishment.'''

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

    if num_rounds == 0: # It's the first round; collude.
        return 'c'
    elif my_last_move == 'c' and their_last_move == 'b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.
