# 👌
with open("Input/Letters/starting_letter.txt") as letter_model:
    contents = letter_model.read()
    with open("Input/Names/invited_names.txt") as names:
        name_list = names.readlines()
        for name in name_list:
            name = name.strip("\n")
            replaced_letter_with_name = contents.replace("[name]", name)
            with open(f"/Output/ReadyToSend/mail_to_{name}.txt", mode="w") as new_file:
                new_file.write(replaced_letter_with_name)

# TO DO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
