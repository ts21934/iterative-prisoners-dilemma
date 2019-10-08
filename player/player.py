'''
Player class that represents a strategy with a move function
'''

class Player:
  def __init__(self, module):
    self.team_name = module.team_name or 'none'
    self.strategy_name = module.strategy_name or 'none'
    self.strategy_description = module.strategy_description or 'none'
    self.moves = ''
    self.score = 0
    def player_move(otherPlayer):
      if not module.move:
        return ' '
      return module.move(self.moves, otherPlayer.moves, self.score, otherPlayer.score)
    self.move = player_move

  def add_score(self, value):
    '''
    Adds value to this Player's score
    '''
    self.score += value

  def add_move(self, move):
    '''
    Adds a new move to this Player's move history
    '''
    self.moves = ''.join([self.moves, move])

  def __repr__(self):
    desc = ' '.join(self.strategy_name.split(' ')[:3])
    return 'Player<team_name: {}, score: {}, strategy: {}>'.format(self.team_name,
        self.score,
        desc)
