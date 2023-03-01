# Eric Cuevas, Andrew Molina
# Assigned Feb 28, Due Mar 2

import random


class Player:

  def __init__(self):
    '''
    Constructs and sorts the list of three Die objects and initializes the player’s points to 0.
    '''
    self.points = 0
    self.dice = [0] * 3

  def get_points(self):
    '''
    Returns the player’s points.
    '''
    return self.points

  def roll_dice(self):
    '''
    Calls roll on each of the Die objects in the dice list and sorts the list.
    '''
    for i in range(len(self.dice)):
      self.dice[i] = random.randint(1, 6)

  def has_pair(self):
    '''
    Returns true if two dice in the list have the same value (uses ==). Increments points by 1.
    '''
    return len(set(self.dice)) == 4

  def has_three_of_a_kind(self):
    '''
    Returns true if all three dice in the list have the same value (uses ==). Increments points by 3.
    '''
    for die in self.dice:
      if self.dice.count(die) >= 3:
        return True
    return False

  def has_series(self):
    '''
    Returns true if the values of each of the dice in the list are in a 
sequence (ex. 1,2,3 or 2,3,4 or 3,4,5 or 4,5,6) (uses -). Increments points by 2.
    '''
    sorted_dice = sorted(self.dice)
    return sorted_dice == list(range(sorted_dice[0], sorted_dice[-1] + 1))

  def add_points(self, points):
    '''
    Add points to the player's score.
    '''
    self.points += points

  def __str__(self):
    '''
    Returns a string in the format: “D1=2, D2=4, D3=6”.
    '''
    return f"Your dice: {', '.join(str(die) for die in self.dice)}"
