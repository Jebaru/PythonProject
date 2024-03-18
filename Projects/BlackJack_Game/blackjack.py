# Day 11 Project:👌

from art import bj_logo
from replit import clear
from random import choices
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add(card_list):
    list_add = sum(card_list)
    perfect_card1 = [10, 11]
    perfect_card2 = [11, 10]
    if perfect_card1 == card_list or perfect_card2 == card_list:
        return 0
    while list_add > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        list_add = sum(card_list)
    return list_add


def final(card_list1, card_list2):
    list1_add = add(card_list1)
    list2_add = add(card_list2)
    while list2_add < 17:
        new_ele = choice(cards)
        com_cards.append(new_ele)
        list2_add += new_ele
    print(
        f"Your cards: {card_list1}, final score: {list1_add}\nComputer's final hand: {card_list2}, final score: {list2_add}")


def compare(user_add, comp_add):
    if user_add == comp_add:
        print("Draw 🙃")
    elif comp_add == 0 or comp_add == 21:
        print("Opponent Win")
    elif user_add == 0 or user_add == 21:
        print("You Win")
    elif user_add < comp_add and comp_add > 21:
        print("Opponent went over. You win 😁")
    elif user_add > 21:
        print("You went over. You lose 😤")
    elif user_add < comp_add:
        print("You Lose 😤")
    elif user_add > comp_add:
        print("You win 😀")


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play == 'y':
    clear()
    print(bj_logo)
    your_cards = choices(cards, k=2)
    com_cards = choices(cards, k=2)
    progress = 'y'
    if add(your_cards) == 0:
        print("You Win")
    elif add(com_cards) == 0:
        print("Opponent Win")
        play = 'n'
    while progress == 'y' and play == 'y':
        print(f"Your cards: {your_cards}, current score: {add(your_cards)}\nComputer's first card: {com_cards[0]}")
        progress = input("Type 'y' to get another card, type 'n' to pass: ")
        if progress == 'y':
            new_card = choice(cards)
            your_cards.append(new_card)
            if add(your_cards) > 21:
                print(
                    f"Your cards: {your_cards}, current score: {add(your_cards)}\nComputer's first card: {com_cards[0]}")
                progress = 'n'
    if progress == 'n' and play == 'y':
        final(your_cards, com_cards)
        your_add = add(your_cards)
        com_add = add(com_cards)
        compare(your_add, com_add)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
