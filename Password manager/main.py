from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    websit = webs.get()
    emails = ems.get()
    password = paswords.get()
    with open(r"C:\Users\garen\Documents\Project Work\Password manager\data.txt", mode="a") as data:  # Added mode="a"
        data.write(f"{websit} | {emails} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#logo
logover_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100 ,image=logover_img)
canvas.grid(column=1,row=0)
#labels
website = Label(text="Website:")
website.grid(column=0,row=1)

Email =  Label(text="Email/Username:")
Email.grid(column=0,row=2)
Password = Label(text="Password:")
Password.grid(column=0,row=3)
#button
Genpass = Button(text="Generate Password")
Genpass.grid(column=2,row=3)
add_button =Button(text = "Add",width=35,command=add)
add_button.grid(column=1, row=4,columnspan=2 )
#entries
webs = Entry(width=35)
webs.grid(column=1,row=1,columnspan=2)
webs.focus()
ems = Entry(width=35)
ems.grid(column=1,row=2,columnspan=2)
ems.insert(0,"garenagbaire@gmail.com")
paswords = Entry(width=21)

paswords.grid(column=1,row=3)
#endloop
window.mainloop()