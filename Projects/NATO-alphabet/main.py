# Day - 26

import pandas
from replit import clear

# TO DO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alpha_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpha_dict = {row.letter: row.code for (index, row) in nato_alpha_csv.iterrows()}
# print(nata_alpha_dict)

# TO DO 2. Create a list of the phonetic code words from a word that the user inputs.
entry = True
while entry:
    clear()
    name = input("Enter the name: ").upper()
    alpha_list = [nato_alpha_dict[n] for n in name]
    print(alpha_list)
    need = input("Type 'y' if you need to enter another name, else type 'n': ").lower()
    if need == 'n':
        entry = False
# ---------------
# Another way
# nata_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nata_alpha)
#
# cust_name = input("Please enter the name:\n").upper()
#
# for name in cust_name:
#     for (index, row) in nata_alpha.iterrows():
#         if row.letter == name:
#             print(f"{name} for {row.code}")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



