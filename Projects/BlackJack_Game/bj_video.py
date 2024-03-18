from art import bj_logo
from replit import clear
from random import choice

# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.


# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return choice(cards)


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(card_list):
    list_add = sum(card_list)

    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
    # instead of the actual score. 0 will represent a blackjack in our game.
    if list_add == 21 and len(card_list) == 2:
        return 0

    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and
    # replace it with a 1. You might need to look up append() and remove().
    if list_add > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        list_add = sum(card_list)
    return list_add


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(score_user, score_comp):
    if score_user == score_comp:
        print("Draw 🙃")
    elif score_comp == 0:
        print("Computer Wins")
    elif score_user == 0:
        print("USer Wins")
    elif score_user > 21:
        print("You went over. You lose 😤")
    elif score_comp > 21:
        print("Opponent went over. You win 😁")
    elif score_user > score_comp:
        print("You win 😀")
    else:
        print("You Lose 😤")


def play_game():
    print(bj_logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
    # then the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")
        if comp_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the
        # deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            progress = input("Type 'y' to get another card, type 'n' to pass: ")
            if progress == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be
    # repeated until the game ends.

    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as
    # long as it has a score less than 17.
    while comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, final score: {user_score}\nComputer's final hand: {computer_cards}, "
          f"final score: {comp_score}")
    compare(user_score, comp_score)


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
