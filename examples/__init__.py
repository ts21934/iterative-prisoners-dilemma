'''
Miles Boswell
Example Class to contain all the example strategies.
Each module has to be loaded, and has a single `move` function.
'''
from . import example0, example1, example2, example3
from . import example4, example5, example6, example7

modules = [
  example0,
  example1,
  example2,
  example3,
  example4,
  example5,
  example6,
  example7
];

def play_iterative_rounds(player1, player2):
  '''
  Plays a random number of rounds (between 100 and 200 rounds)
  of the iterative prisoners' dilemma between two strategies.
  player1 and player2 are modules.
  Returns 4-tuple, for example ('cc', 'bb', -200, 600)
  but with much longer strings
  '''
  number_of_rounds = random.randint(100, 200)
  moves1 = ''
  moves2 = ''
  score1 = 0
  score2 = 0
  for round in range(number_of_rounds):
      score1, score2, moves1, moves2 = play_round(player1, player2, score1, score2, moves1, moves2)
  return (score1, score2, moves1, moves2)
