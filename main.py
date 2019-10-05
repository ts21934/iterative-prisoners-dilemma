'''
Main driver application to run all modules
'''
from player import PlayerGroup
from examples import modules as example_modules

if __name__ == '__main__':
  pg = PlayerGroup(example_modules)
  pg.run(num_rounds=100)
