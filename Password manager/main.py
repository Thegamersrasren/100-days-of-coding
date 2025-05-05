from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def randopass():
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)
    
    password = "".join(password_list)
    paswords.delete(0, END)  # Clear field before inserting
    paswords.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    websit = webs.get()
    emails = ems.get()
    password = paswords.get()
    
    if len(websit) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Do not leave any empty Fields")
    else:
        is_ok = messagebox.askokcancel(title=websit, 
                                     message=f"These are the details entered:\nEmail: {emails}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open(r"C:\Users\garen\Documents\Project Work\Password manager\data.txt", "a") as data:
                data.write(f"{websit} | {emails} | {password}\n")
                webs.delete(0, END)
                paswords.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
logover_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100 ,image=logover_img)
canvas.grid(column=1,row=0)

# Labels and Entries
website = Label(text="Website:")
website.grid(column=0, row=1)
webs = Entry(width=35)
webs.grid(column=1, row=1, columnspan=2)
webs.focus()

Email = Label(text="Email/Username:")
Email.grid(column=0, row=2)
ems = Entry(width=35)
ems.grid(column=1, row=2, columnspan=2)
ems.insert(0, "garenagbaire@gmail.com")

Password = Label(text="Password:")
Password.grid(column=0, row=3)
paswords = Entry(width=21)
paswords.grid(column=1, row=3)

# Buttons
Genpass = Button(text="Generate Password", command=randopass)
Genpass.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()