# creating a program to help spell out name using nato phonetic aplhabet

# importing panda and loading up the csv datafile where alphabet and its corresponding word
import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_alphabet.head(5))

# Loop through rows of a data frame to create a dictionary to store letter its word value
# using dictionary comprehension
alpha_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("enter the word you want to create a phonetic code")

# using list comprehension
user_output_list = [alpha_dict[letter] for letter in user_input.upper()]
print(user_output_list)

