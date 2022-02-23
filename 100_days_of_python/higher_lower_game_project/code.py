
#WIP..

import random
from art import logo
from game_data import data

score = 0
# compare_a = data[random_number]
# against_b = data[random_number]
random_number = random.randint(1,50)
data_for_a = data[random_number]
data_for_b = data[random_number]


def answer():
  if data_for_a['follower_count'] > data_for_b['follower_count']:
    return 'a'
  elif data_for_a['follower_count'] < data_for_b['follower_count']:
    return 'b'

print(answer())

# guess = input("Who has more followers? Type A or B: ")


    

# print(f"Compare A: {data_for_a['name']}, {data_for_a['description']}, from {data_for_a['country']}")


# print(f"Against B: {data_for_b['name']}, {data_for_b['description']}, from {data_for_b['country']}")
