'''
Iterative Prisoner's Dillema Team Submission

In this file, you MUST define the following:

Variables:
  - team_name:            a string with your team's name
  - strategy_name:        a string with your team's strategy name
  - strategy_description: a string with your team's strategy name

Functions:
  - move(my_last_move, their_last_move):
    your team's implementation of your strategy (see move() docstring)
'''

team_name = 'MILES'
strategy_name = 'Tit for Tat'
strategy_description = 'Begin with a collude, then mirror opponent\'s move'

def move(my_last_move, their_last_move):
    '''
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    '''
    if my_last_move == '' and their_last_move == '':
        return 'c'
    return their_last_move

if __name__ == '__main__':
  print(move('c', 'c'))
  print(move('c', 'b'))
  print(move('b', 'c'))
  print(move('b', 'b'))
