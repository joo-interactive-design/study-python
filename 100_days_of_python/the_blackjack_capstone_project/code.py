
#Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

