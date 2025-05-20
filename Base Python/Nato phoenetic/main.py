import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato = {row.letter: row.code for (index, row) in phonetic.iterrows()}
# while True:
#     word = input("Type in the word ").upper()
#     try:
#         code = [Nato[letter] for letter in word]
        
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print (code)
print(Nato)
