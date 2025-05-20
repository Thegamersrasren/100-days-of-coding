from tkinter import *

def button_clicked():
    miles = float(input.get())  # Convert input to float
    km = miles * 1.609
    Label3.config(text=f"{km:.2f}")  # Display km with 2 decimal places

window = Tk()
window.title("Unit converter")
window.config(padx=20,pady=20)

# Entry with Miles label
input = Entry(width=7)
input.grid(column=1, row=0)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

is_equals_to = Label(text="is equals too")
is_equals_to.grid(column= 0, row= 1)

# Result display (0 and Km label)
Label3 = Label(text="0")
Label3.grid(column=1, row=1)

Label2 = Label(text="Km")
Label2.grid(column=2, row=1)

Label4 = Label(text="is equals to ")
Label2.grid(column=1, row=2)
# Calculate button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()