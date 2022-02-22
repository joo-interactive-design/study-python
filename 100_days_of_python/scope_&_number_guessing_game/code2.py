import random
#from art import logo
#from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#make a function to check user's guess against the actual answer
def check_answer(answer, user_guess,remaining_turns):
  """checks answer against guess. returns the number of turns remaining"""
  if answer == user_guess:
    print("That's right. You win!") 
  elif answer > user_guess:
    remaining_turns - 1
    print("Too low.Guess again.")
    return remaining_turns - 1
  elif answer > user_guess:
    remaining_turns - 1
    print("Too high.Guess again.")
    return remaining_turns - 1

#make a function to set difficulty
def choose_difficulty():
  game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  #choose a random number between 1 and 100
  answer = random.randint(1,100)
  print(f"Pssst, the correct answer is {answer}")
  
  remaining_turns = choose_difficulty() 
 
  #check_answer(answer, user_guess)
  #create a variable called user_guess and set it as 0("undefined name "user_guess" if there is no the variable outside of the while loop below)
  user_guess = 0
  while user_guess != answer:
    print(f"you have {remaining_turns} attemps remaining to guess the number")
    #let user guess the number
    user_guess = int(input("Make a guess: "))
    
    remaining_turns = check_answer(answer, user_guess, remaining_turns)
    if remaining_turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif user_guess != answer:
      print("Guess again.")  
    
        
    
game()
 
  

    
