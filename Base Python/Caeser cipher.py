should_continue = True
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def encrypt(word, shift):
    cipher = ""  
    for letter in word:
        if letter in alphabet:
            shifted = (alphabet.index(letter) + shift) % 26
            cipher += alphabet[shifted]
        else:
            cipher += letter  
    print("Here is the encrypted cipher:", cipher)

def decrypt(word, shift):
    cipher = ""  
    for letter in word:
        if letter in alphabet:  
            shifted = (alphabet.index(letter) - shift) % 26
            cipher += alphabet[shifted]
        else:
            cipher += letter 
    print("Here is the encrypted cipher:", cipher)



while should_continue:
    word = input("Type in the word: ").lower()
    try:
        shift = int(input("How much do you want to shift by? ")) 
        shift = shift % 26
    except ValueError:
        print("Error please put in a variable")
        continue
    
    choice = input("Would you like to encode or decode? ").lower()
        
    if choice == "decode":
        decrypt(word, shift)
        
    elif choice == "encode":
        encrypt(word, shift)
    else:
        print("invalid choice. Please enter encode or decode")

    Redo = input("Do you wish to do it again Yes or no ").lower()
    if Redo == "no":
        should_continue = False
        print("Goodbye")