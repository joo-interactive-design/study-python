

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
    return cards.remove(11).append(1)
    
  return sum(cards)
  

#Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
game_end = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not game_end:
  #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"your card is {user_cards}, current score: {user_score}")
  print(f"computer card is {computer_cards[0]}")

  if user_score == 0 or computer_score == 0 or user_score > 21:
    game_end = True
    #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
  else:
    add_another_card =input("Type 'y' to get another card, or type 'n' to end the game: ").lower()
    if add_another_card == "y":
       user_cards.append(deal_card())
    if add_another_card == "n":
      game_end = True
    
    
