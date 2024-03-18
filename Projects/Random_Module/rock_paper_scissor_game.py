# Day 4 Project👌

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
com_chose = random.randint(0, 2)
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissor)
else:
    quit("Choose invalid number ^^")
print("Computer Chose:")
if com_chose == 0:
    print(rock)
elif com_chose == 1:
    print(paper)
else:
    print(scissor)
# if choose == 0:
#     if com_chose == 0:
#         print("It's  a draw 🙂")
#     elif com_chose == 1:
#         print("You lose 😏")
#     else:
#         print("You Win! 😊")
# elif choose == 1:
#     if com_chose == 1:
#         print("It's  a draw 🙂")
#     elif com_chose == 2:
#         print("You lose 😏")
#     else:
#         print("You Win! 😊")
# else:
#     if com_chose == 2:
#         print("It's  a draw 🙂")
#     elif com_chose == 0:
#         print("You lose 😏")
#     else:
#         print("You Win! 😊")
# game_list = [0, 1, 2]
# choose_index = game_list.index(choose)
# com_chose_index = game_list.index(com_chose)
# print(choose_index, com_chose_index)
# if choose == com_chose: # 0==0 1==1 2==2
#     print("It's  a draw 🙂")
# elif game_list[choose-1] == game_list[com_chose]:
#     print("You Win! 😊")
# else:
#     print("You lose 😏")
if choose == com_chose:
    print("It's a draw 🙂")
elif choose == 0 and com_chose == 2:
    print("You Win! 😊")
elif choose > com_chose:
    print("You Win! 😊")
else:
    print("You lose 😏")