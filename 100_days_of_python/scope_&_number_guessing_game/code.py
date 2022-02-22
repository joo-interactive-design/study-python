import random
#from art import logo
#from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#make a function to check user's guess against the actual answer
def check_answer(answer, user_guess):
  if answer == user_guess:
      print("That's right. You win!") 
  elif answer > user_guess:
      print("Too low.Guess again.")
  elif answer > user_guess:
      print("Too high.Guess again.")

#make a function to set difficulty
def choose_difficulty():
  game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

#print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#choose a random number between 1 and 100
answer = random.randint(1,100)
print(f"Pssst, the correct answer is {answer}")

remaining_turns = choose_difficulty() 
print(f"You have {remaining_turns} attempts remaining to guess the number.")

#Let the user guess a number
user_guess = int(input("Make a guess: "))
check_answer(answer, user_guess)

while user_guess != answer:
  remaining_turns -= 1
  user_guess = int(input("Make a guess: "))
  check_answer(answer, user_guess)
  print(f"You have {remaining_turns} attempts remaining to guess the number.")

