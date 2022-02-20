
import random

#Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
#Create a function called calculate_score() that takes a List of cards as input 
def calculate_score(cards):
 #take a list of cards and return the score calculated from the card
  if sum(cards)==21 and len(cards)==2:
    #0 is Blackjack
    return 0


  #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11).append(1)
    
  return sum(cards)
  
#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(computer_score, user_score):
  if computer_score == user_score:
    return "draw"
  elif computer_score == 0:
    return "lose"
  elif user_score > 21:
    return "lose"
  elif user_score == 0: 
    return "win!"
  elif computer_score > 21 :
    return "win!"
  elif user_score > computer_score:
    return "win!"
  else:
    return "lose"
    
#create a funcion called play_game(), so user can re-play the game.
def play_game():   
  user_cards = []
  computer_cards = []
  game_end = False
  
  #Deal the user and computer 2 cards each using deal_card() and append().
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your card is {user_cards}, current score: {user_score}")
    print(f"computer card is {computer_cards[0]}")
  
  #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_end = True
      #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else:
      add_another_card =input("Type 'y' to get another card, or type 'n' to end the game: ").lower()
      if add_another_card == "y":
         user_cards.append(deal_card())
      else:
        game_end = True
  
  #Once the user is done, the computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(computer_score, user_score))  
  
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
