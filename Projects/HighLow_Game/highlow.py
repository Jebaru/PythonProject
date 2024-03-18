# Day 14 Project👌
# import statements
from art import hl_logo
from random import choice
from hlgame_data import data
from art import vs
from replit import clear


def get_dict():
    """This function generates a random value from the list and returns a dictionary"""
    return choice(data)


def score(value, compare_1, compare_2):
    """Compares the follower count of each data and returns the score"""
    if value == 'a' and compare_1['follower_count'] > compare_2['follower_count']:
        return 1
    elif value == 'b' and compare_1['follower_count'] < compare_2['follower_count']:
        return 1
    else:
        return 0


#
# def first_value_compare(fist_data, second_data):
#     """Returns the Dict_1 that has higher follower_count"""
#     if fist_data['follower_count'] > second_data['follower_count']:
#         return fist_data
#     else:
#         return second_data


score_point = 1
result = 0
data_1 = get_dict()
high_score = 0
while score_point:
    clear()
    # Logo of Higher Lower game
    print(hl_logo)
    if high_score:
        print(f"High Score: {high_score}")
    if result > 0:
        print(f"You're right! Current Score: {result}")
    # Getting a random value from the list data
    data_2 = get_dict()
    while data_2 == data_1:
        data_2 = get_dict()
    print(f"Compare A: {data_1['name']}, a {data_1['description']}, from {data_1['country']}.\n{vs}"
          f"\nAgainst B: {data_2['name']}, a {data_2['description']}, from {data_2['country']}.")
    option = input("Who has more followers? Type 'A' or 'B': ").lower()
    score_point = score(option, data_1, data_2)
    result += score_point
    if score_point:
        data_1 = data_2
        # data_1 = first_value_compare(data_1, data_2)
    else:
        print(f"Oops! You're wrong...⚠️ Your Final Score is {result}\nYou Can do better. So don't give up try again.")

    if not score_point and input("Do you wanna play again. Type 'y' if yes else 'n': ") == 'y':
        score_point = 1
        if result > high_score:
            high_score = result
        result = 0
