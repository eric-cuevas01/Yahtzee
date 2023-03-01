# Eric Cuevas, Andrew Molina
# Assigned Feb 28, Due Mar 2

import random


class Die:

  def __init__(self, sides=6):
    '''
    Assigns the number of sides from the value passed in. Set value to 0 or to the returned value of roll().
    '''
    self.sides = sides
    self.value = self.roll()

  def roll(self):
    '''
    Generate a random number between 1 and the number of sides and assign it to the Die’s value.  Return the value.
    '''
    self.value = random.randint(1, self.sides)
    return self.value

  def __str__(self):
    '''
    Return the Die’s value as a string.
    '''
    return str(self.value)

  def __lt__(self, other):
    '''
    Return true if the value of self is less than the value of other. 
    '''
    return self.value < other.value

  def __eq__(self, other):
    '''
    Return true if both the values of self and other are equal.
    '''
    return self.value == other.value

  def __sub__(self, other):
    '''
    Return the difference between the value of self and the value of other.
    '''
    return self.value - other.value
