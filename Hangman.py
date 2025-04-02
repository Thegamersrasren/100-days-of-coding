import random
word=["mango","driving","reading","nether"]
chosen_word = random.choice(word)
print (chosen_word)
placeholder= str()
for position in range(len(chosen_word)):
    placeholder += "_"
print (placeholder)
display = ""
gameover = False
lives = len(chosen_word)
while not gameover:
    newdisplay = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            newdisplay += letter
        else:
            newdisplay += "_"
        display = newdisplay

    print(display)
    if "_" not in display:
        print("You Win")
        gameover = "true"
    if lives <0 :
        print("You lose")
        

   