team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'

def move(my_last_move, their_last_move):
    '''
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    '''

    #This example player always betrays.
    return 'b'
