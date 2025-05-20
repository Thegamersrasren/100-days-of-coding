from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
words_dict = []

#-----------DATA SETUP------------#
try:
    words = pd.read_csv("words_to_learn.csv")  # Fixed filename to match what you save
    words_dict = words.to_dict(orient="records")
except FileNotFoundError:
    words = pd.read_csv(r"C:\Users\garen\Documents\Project Work\Flashcard\data\french_words.csv")
    words_dict = words.to_dict(orient="records")

randomword = {"French": "", "English": ""}
current_after_id = None  # To track the after() timer

# Functions
def failchangeword():
    global randomword, current_after_id
    
    # Cancel any pending flip
    if current_after_id:
        window.after_cancel(current_after_id)
    
    if words_dict:  # Check if there are words left
        randomword = random.choice(words_dict)
        canvas.itemconfig(changew, text=randomword["French"], fill="black")
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(old, image=front_img)
        current_after_id = window.after(3000, flip_card)
  
def passchangeword():
    global randomword, current_after_id, words_dict
    
    # Cancel any pending flip
    if current_after_id:
        window.after_cancel(current_after_id)
    
    if words_dict:  # Check if there are words left
        randomword = random.choice(words_dict)
        canvas.itemconfig(changew, text=randomword["French"], fill="black")
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(old, image=front_img)
        
        # Remove the current word and save the updated list
        words_dict.remove(randomword)
        pd.DataFrame(words_dict).to_csv("words_to_learn.csv", index=False)  # Fixed filename and added index=False
        
        # Start new timer
        current_after_id = window.after(3000, flip_card)

def flip_card():
    global back_img
    back_img = PhotoImage(file=r"C:\Users\garen\Documents\Project Work\Flashcard\images\card_back.png")
    canvas.itemconfig(old, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(changew, text=randomword["English"], fill="white")

#-----------UI SETUP------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Images
front_img = PhotoImage(file=r"C:\Users\garen\Documents\Project Work\Flashcard\images\card_front.png")
back_img = PhotoImage(file=r"C:\Users\garen\Documents\Project Work\Flashcard\images\card_back.png")
correct = PhotoImage(file=r"C:\Users\garen\Documents\Project Work\Flashcard\images\right.png")
incorrect = PhotoImage(file=r"C:\Users\garen\Documents\Project Work\Flashcard\images\wrong.png")

# Canvas Setup
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
old = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
changew = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right = Button(image=correct, highlightthickness=0, command=passchangeword)
right.grid(row=1, column=1)
wrong = Button(image=incorrect, highlightthickness=0, command=failchangeword)
wrong.grid(row=1, column=0)

# Start with first word


# Start the app
window.mainloop()