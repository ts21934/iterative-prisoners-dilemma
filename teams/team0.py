'''
Iterative Prisoner's Dillema Team Submission

In this file, you MUST define the following:

Variables:
  - team_name:            a string with your team's name
  - strategy_name: a string with your team's strategy name
  - strategy_description: a string with your team's strategy name

Functions:
  - move(my_history, their_history, my_score, their_score):
    your team's implementation of your strategy
    (see move() docstring)
'''

team_name = 'YOUR TEAM NAME'
strategy_name = 'however you want to describe your strategy'
strategy_description = 'How does this strategy decide?'

def move(my_history, their_history, my_score, their_score):
  '''
  Make a move based on your and your opponent's previous moves, and your and their
  scores.

  @param my_history a string representing your move history, where the first index (0)
                      is your first move and the last index (-1) is your most recent move
  @param their_history a string representing your opponent's move history, where the
                      first index (0) is their first move and the last index (-1) is their
                      most recent move
  @param my_score     an int representing your current score
  @param their_score  an int representing your opponent's current score
  @return             string representing your move for this turn, based on both players
                      move histories and their scores ('c' to collude, 'b' to betray)
  '''

  return 'c'

if __name__ == '__main__':
  move()
