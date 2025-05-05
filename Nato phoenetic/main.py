
import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato = {row.letter: row.code for (index, row) in phonetic.iterrows()}
word = input("Type in the word ").upper()
code = [Nato[letter] for letter in word]

print (code)
