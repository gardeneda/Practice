# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    sentences = letter.readlines()

with open("./Input/Names/invited_names.txt", mode="r+") as people:
    names = people.readlines()


new_names = []

for name in names:
    x = name.strip()
    new_names.append(x)

new_sentences = sentences.copy()
# new_sentences = sentences will make the change that happens to both be applied to both at the same time.

for number in range(len(names)):
    with open(f"./Output/ReadyToSend/{new_names[number]}.txt", mode="w") as final_copy:
        new_sentences[0] = sentences[0].replace("[name]", new_names[number])
        # print(f"This is the original list, sentences ={sentences}") (Used to check if [name] was being replaced)
        str_sentences = ''.join(new_sentences)
        final_copy.write(str_sentences)

# -------------------------------------------------------------------------

PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt", mode="r+") as people:
    names = people.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_copy:
            final_copy.write(new_letter)

