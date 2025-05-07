from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD CHARACTER SETS ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password and copy to clipboard"""
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    paswords.delete(0, END)
    paswords.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save password data to JSON file"""
    websit = webs.get()
    emails = ems.get()
    password = paswords.get()
    
    new_data = {
        websit: {
            "email": emails,
            "password": password,
        }
    }

    if len(websit) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(r"C:\Users\garen\Documents\Project Work\Password manager\data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(r"C:\Users\garen\Documents\Project Work\Password manager\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(r"C:\Users\garen\Documents\Project Work\Password manager\data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            webs.delete(0, END)
            paswords.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    websit = webs.get()
    try:
        with open(r"C:\Users\garen\Documents\Project Work\Password manager\data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if websit in data:
            email = data[websit]["email"]
            password = data[websit]["password"]
            messagebox.showinfo(title=websit, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {websit} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
Email = Label(text="Email/Username:")
Email.grid(row=2, column=0)
Password = Label(text="Password:")
Password.grid(row=3, column=0)

# Entries
webs = Entry(width=21)
webs.grid(row=1, column=1)
webs.focus()
ems = Entry(width=35)
ems.grid(row=2, column=1, columnspan=2)
ems.insert(0, "garenagbaire@gmail.com")
paswords = Entry(width=21)
paswords.grid(row=3, column=1)

# Buttons
search = Button(text="Search", width=13, command=find_password)
search.grid(row=1, column=2)
Genpass = Button(text="Generate Password", command=generate_password)
Genpass.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()