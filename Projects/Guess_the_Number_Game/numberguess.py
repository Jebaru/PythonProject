# Day 12 Project👌
from art import no_guess_logo
from random import randint
from replit import clear

EASY_LEVEL = 10
HARD_LEVEL = 5


def guessing(difficulty, guessed_num):
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    crt = False
    while attempts > 0 and not crt:
        guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
        if guess < guessed_num:
            print("Too low.")
            if attempts > 1:
                print("Guess again.")
        elif guess > guessed_num:
            print("Too high.")
            if attempts > 1:
                print("Guess again.")
        else:
            print(f"You got it! The answer was {guessed_num}.")
            crt = True
        attempts -= 1
    if attempts == 0 and not crt:
        print(f"Game Over 👾. The guessed number is: {guessed_num}")


play = 'y'
while play == 'y':
    clear()
    print(no_guess_logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking a number between 1 and 100.")
    guess_no = randint(1, 100)
    # print(f"Computer Guessed number is: {guess_no}")
    level_choose = True
    while level_choose:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy' or level == 'hard':
            guessing(level, guess_no)
            level_choose = False
        else:
            print("Please enter appropriate level")

    play = input("Do you wanna play number guessing Game again. Type 'y' to play or 'n' to exit.")

