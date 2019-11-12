team_name = 'E4'
strategy_name = 'Use early history'
strategy_description = '''\
Collude first round. Compare all rounds to the previous round and
assume opponent will behave the same as the first time the previous
round's result occurred. If the previous round's result never has
happened, collude except after being severly punished.'''

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
    else:
        # No match found
        if my_last_move == 'c' and their_last_move == 'b':
            return 'b' # Betray if they were severely punished last time
        else:
            return 'c' # Otherwise collude.
