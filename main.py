'''
Main driver application to run all modules
'''
import argparse
from player import PlayerGroup
from examples import modules as example_modules
from teams import modules as team_modules

if __name__ == '__main__':
  # parse command line arguments
  parser = argparse.ArgumentParser(description='Iterative Prisoner\'s Dilemma Game')
  parser.add_argument('-e', '--example', action='store_true')
  parser.add_argument('-n', '--rounds', type=int,
      help='Number of rounds to run the Simulation default=100', default=100)
  args = parser.parse_args()

  # run game simulation
  modules = example_modules if args.example else team_modules
  pg = PlayerGroup(modules)
  pg.run(num_rounds=args.rounds)
