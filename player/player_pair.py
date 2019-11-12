'''
Implements a pairing of two Players that play against each other
'''

class PlayerPair:
  def __init__(self, p1, p2):
    '''
    Constructor accepts two Players
    '''
    self.players = (p1, p2)

  def play_round(self):
    '''
    Simulates a single round of play between this and another Player object
    '''
    p1, p2 = self.players
    p1_action, p2_action = p1.move(p2), p2.move(p1)
    # clean up the p1_action returns if something went wrong
    def parse_action(action_str):
      if (type(action_str) != str) or (len(action_str) != 1):
        return ' '
      return action_str
    p1_action, p2_action = parse_action(p1_action), parse_action(p2_action)
    # Change scores based upon player result.
    result = ''.join([p1_action, p2_action])
    self.handle_scores(p1_action, p2_action)
    # Append the result to the previous histories.
    p1.add_move(p1_action)
    p2.add_move(p2_action)

  def handle_scores(self, p1_action, p2_action) :
    p1, p2 = self.players
    REWARD = 5
    SENTENCE = 3
    PUNISHMENT = 1
    BETRAYED = 0

    if p1_action == 'c':
      if p2_action == 'c':
        # both players colluded, get normal sentence
        p1.add_score(SENTENCE)
        p2.add_score(SENTENCE)
      elif p2_action == 'b':
        # p2 betrayed p1, release p2 and give p1 severe sentence
        p1.add_score(BETRAYED)
        p2.add_score(REWARD)
      else:
        # p2 had an error
        print('{} had an error: "{}"'.format(p2, p2_action))
    elif p1_action == 'b':
      if p2_action == 'c':
        # p1 betrayed p2, release p1 and give p2 severe sentence
        p1.add_score(REWARD)
        p2.add_score(BETRAYED)
      elif p2_action == 'b':
        # both players betrayed each other, give both players punishment
        p1.add_score(PUNISHMENT)
        p2.add_score(PUNISHMENT)
      else:
        # p2 had an error
        print('{} had an error: "{}"'.format(p2, p2_action))
    else:
      # p1 had an error
      print('{} had an error: "{}"'.format(p1, p1_action))

  def __repr__(self):
    p1, p2 = self.players
    return 'PlayerPair<{} vs {}>'.format(p1.team_name, p2.team_name)
