import random

MAX_INCORRECT_GUESS = 10


class Player:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def getName(self):
    return self.name

  def getScore(self):
    return self.score

  def setName(self, name):
    self.name = name

  def setScore(self, score):
    self.score = score


#reads in puzzles from a file and returns the puzzles in a list
def read_wheel_puzzles():
  open_file = open("wheel_puzzles.txt", "r")

  wheel_puzzles = list()
  for line in open_file:
    wheel_puzzles.append(line.rstrip())

  open_file.close()

  return wheel_puzzles

#reads in values from the file and returns the values in a list
def read_wheel_values():
  open_file = open("wheel_values.txt", "r")

  wheel_values = list()
  for line in open_file:
    wheel_values.append(line.rstrip())

  open_file.close()

  return wheel_values

#picks a random value from wheel_values list
def spin_wheel (wheel_values):
  return random.choice(wheel_values)

#picks a random puzzle from the wheel_puzzles list
def pick_random_puzzle(wheel_puzzles):
  return random.choice(wheel_puzzles)

#turns a puzzle into underscores
#For example, if the puzzle is:
#UNC rocks the function will return
#___ _____
def turn_puzzle_into_underscores(random_puzzle):
  solved_puzzle = list()
  for character in random_puzzle:
    if character == " ":
      solved_puzzle.append(" ")
    else:
      solved_puzzle.append("_")

  return solved_puzzle

#returns true if guess is in puzzle, otherwise returns false
def is_guess_in_puzzle (user_guess, puzzle):
  if user_guess in puzzle:
    return True

  return False

#given a letter (for example s), the random puzzle (for example UNC rocks), and the solved puzzle (for example, U__ rock_), this function will replace all
#underscores with the letter (for example the following will be returned U__ rocks)
def show_letter_in_solved_puzzle(letter, solved_puzzle, random_puzzle):
  index = 0
  for r in random_puzzle:
    if r.lower() == letter.lower():
      solved_puzzle[index] = r

    #increase the index variable by 1
    index += 1

  return ' '.join(solved_puzzle)

#computes player score
def compute_player_score (number_of_times_letter_is_in_puzzle, spin_value):
  return (int(number_of_times_letter_is_in_puzzle) * int(spin_value))

#returns true if the user has guessed all the letters in the puzzle, otherwise returns false
def puzzle_is_solved(puzzle):
  if "_" in puzzle:
    return False

  return True

#returns the correct player
def change_player(current_player, player1, player2, player3):
    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player3
    else:
        current_player = player1
    return current_player


def play_game(puzzle_with_underscores, random_puzzle, wheel_values):
  guess_list = []
  #ask all three players for their name
  name = input("Player 1 please enter your name: ")
  player1 = Player(name, 0)


  name = input("Player 2 please enter your name: ")
  player2 = Player(name, 0)

  name = input("Player 3 please enter your name: ")
  player3 = Player(name, 0)

  #current_player variable keeps track of the current player's turn, before the game start, it's the 1st player's turn
  current_player = player1
  # current_player_score = current_player.setScore()
  # current_player_score = compute_player_score(number_of_times_letter_is_in_puzzle, spin_value)
  print(current_player.getName(),"it is your turn.")
  print(random_puzzle)
  game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")
  #initial_solved_puzzle = turn_puzzle_into_underscores(random_puzzle)
  initial_solved_puzzle = puzzle_with_underscores
  solved_puzzle = initial_solved_puzzle
  while puzzle_is_solved(solved_puzzle) == False:

    if game_choice == "spin":
      if int(wheel_values) == -1:
        score = compute_player_score(0,wheel_values)
        current_player.setScore(score)
        print("Your spin is: Lose Turn and go bankrupt")
        current_player = change_player(current_player, player1, player2, player3)
        print(current_player.getName(), "it is your turn, your score is: ", str(current_player.getScore()))
        game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")
      elif int(wheel_values) == -2:
        print("Your spin is: Lose Turn")
        current_player = change_player(current_player, player1, player2, player3)
        print(current_player.getName(), "it is your turn., your score is: ", str(current_player.getScore()))
        game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")
      else:
        print("Your spin is: ",str(wheel_values))
        user_guess = input("Please guess a vowel or a consonant: ")


        if user_guess not in random_puzzle.lower():
          print("There is not a ", user_guess, "in the puzzle")
          current_player = change_player(current_player, player1, player2, player3)
          print(current_player.getName()," it is your turn")
          game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")

        elif guess_list is not None and user_guess in guess_list:
          print("This letter has already been guessed")
          current_player = change_player(current_player, player1, player2, player3)
          print(current_player.getName(), "you have ", str(current_player.getScore())," dollars.")
          game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")

        elif user_guess in random_puzzle.lower():
          number_of_times_letter_is_in_puzzle = 0
          for r in random_puzzle:
            if r.lower() == user_guess.lower():
              number_of_times_letter_is_in_puzzle += 1

          score = compute_player_score(number_of_times_letter_is_in_puzzle, wheel_values)
          current_player.setScore(current_player.getScore() + score)

          solved_puzzle = show_letter_in_solved_puzzle(user_guess,initial_solved_puzzle,random_puzzle)
          print(solved_puzzle)
          if puzzle_is_solved(solved_puzzle):
            print("You win!")
            print("You won ", str(current_player.getScore())," dollars total!")
            print("The phrase was",random_puzzle)
            break
          print(current_player.getName(), "you have ", str(current_player.getScore())," dollars.")
          game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")
        guess_list.append(user_guess)

    elif game_choice == "solve":
      user_guess = input("Please enter the letters of the puzzle: ")
      if puzzle_is_solved(user_guess):
        print("You win!")
        print("You won ", str(current_player.getScore())," dollars total!")
        print("The phrase was",random_puzzle)
        #solved_puzzle = show_letter_in_solved_puzzle(user_guess,initial_solved_puzzle,random_puzzle)
        break

      else:
        print("That is not the correct puzzle.")
        current_player = change_player(current_player, player1, player2, player3)
        print(current_player.getName(), "you have ", str(current_player.getScore())," dollars.")
        game_choice = input("What would you like to do Spin (spin) or Solve (solve): ")

def main():
  wheel_values = read_wheel_values()
  wheel_puzzles = read_wheel_puzzles()
  puzzle = pick_random_puzzle(wheel_puzzles)
  values = spin_wheel(wheel_values)

  puzzle_with_underscores = turn_puzzle_into_underscores(puzzle)

  play_game(puzzle_with_underscores, puzzle, values)

main()
