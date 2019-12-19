'''
Class composed of Players with methods for playing rounds
'''
from .player import Player
from .player_pair import PlayerPair

class PlayerGroup:
  def __init__(self, modules):
    self.players = [Player(m) for m in modules]

  def create_pairs(self):
    '''
    NOTE: only works with even numbers of players (two to a pair)
    '''
    pairs = []
    for i, p1 in enumerate(self.players):
      for j in range(i):
        pairs.append(PlayerPair(p1, self.players[j]))
    return pairs

  def run(self, num_rounds=1):
    pairs = self.create_pairs()
    for i in range(num_rounds):
      for pair in pairs:
        pair.play_round()
    self.print_players()

  def print_players(self):
    for p in self.players:
      print(p)