import random
word = ["mango", "driving", "reading", "nether", "radian", "leave","more","endless","wonderful","finale"]
chosen_word = random.choice(word)
print(chosen_word)
stage= [ '''+---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''','''  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========''','''  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''',''' +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',''' +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''+---+
     |   |
     O   |
         |
         |
         |
   =========''','''+---+
     |   |
         |
         |
         |
         |
   =========''']

    

placeholder = str()
wordlength = len(chosen_word)
for position in range(wordlength):
    placeholder += "_"


gameover = False

correctletter = []

lives = 6
print("Welcome to Hangman")
print(placeholder)
while not gameover:
    
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correctletter.append(letter)
        elif letter in correctletter:
            display += letter
        else:
            display += "_"
    if guess  not in chosen_word:
            lives -= 1
            print (stage[lives])
            print("(===================",lives,"/6 LIVES LEFT===================)")
            if lives == 0 :
                gameover = True
                print("Game Over! The correct word was:", chosen_word)
                break
    
        
    print("Word to be guessed",display)
    
        
          
    
        

    if "_" not in display:
        print("You Win")
        break
    