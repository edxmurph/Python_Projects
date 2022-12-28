# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

#TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
"""There's 2 different ways to do this."""

### First way.
# while True:
#     user_input = input("Please enter a word: ").upper()
#     try:
#         phonetic_code = [phonetic_dict[letter] for letter in user_input]
#         break
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")

# print(phonetic_code)


### Second way.
def generate_phonetic_code():
    user_input = input("Please enter a word: ").upper()
    try:
        phonetic_code = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_code()
    else:
        print(phonetic_code)

generate_phonetic_code()