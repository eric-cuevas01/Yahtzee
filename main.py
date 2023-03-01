# Eric Cuevas, Andrew Molina
# Assigned Feb 28, Due Mar 2
# A dice game that awards the user points for pair, three-of-a-kind, or a series. The objective of the game is to roll certain combinations of numbers with three dice. At each turn you throw dice trying to get a good combination of numbers; different combinations give different scores.

import check_input
from player import Player


def take_turn(player):
  '''
  Roll the player’s dice, display the dice, check for and display any win types (pair, series, three-of-a-kind), and display the updated score.    '''
  player.roll_dice()
  print(f"\nRolling the dice...\n{player}")
  points = 0
  if player.has_pair():
    print("You got a pair! +1 points!")
    points += 1
  if player.has_three_of_a_kind():
    print("You got three-of-a-kind! +3 points!")
    points += 3
  if player.has_series():
    print("You got a series! +2 points!")
    points += 2
  player.add_points(points)
  print(f"Your score is now {player.get_points()}")
  return points


def main():
  '''
  Construct a player object, and then repeatedly call take_turn until the user chooses to end the game. Display the final points at the end of the game.
  '''
  player = Player()
  total_points = 0
  while True:
    if not check_input.get_yes_no("Do you want to take a turn? "):
      break
    points = take_turn(player)
    total_points += points
  print(f"\nThanks for playing! Your final score is {player.get_points()}.")


main()