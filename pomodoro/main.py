from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
worker = None
marks = "" 
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)
#tomato
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timertext =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))  # Fixed "Bold" to "bold"
canvas.pack()  
#Labels
timer = Label(text="Timer",fg=GREEN, font=(FONT_NAME,25,"bold"),bg= YELLOW)
timer.place(x=50, y=-40)
checks = Label(fg=GREEN, font=(FONT_NAME, 10), bg=YELLOW)
checks.place(x=70,y= 230)
#Buttons

def start_timer():
    global reps
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Break",fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer.config(text="Work",fg=GREEN)
        
    
start = Button(text="Start",command=start_timer)
start.place(x=-20,y=220)


#countdown
# def seconds(second):
#     # window.after(1000,seconds,second-1)
#     # return(second)
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f"0{count_sec}"
    canvas.itemconfig(timertext, text=f"{count_min}:{count_sec}")
    if count> 0 :
        global worker
        worker = window.after(10,count_down,count-1)
    else:
        start_timer()
        global marks
        work = math.floor(reps/2)
        for _ in range(work):
            marks += "✓"
            checks.config(text=marks)
#reset
def reset ():
    global reps,marks
    window.after_cancel(worker)
    marks = ""
    checks.config(text="")
    timer.config(text="Timer")
    canvas.itemconfig(timertext, text="00:00")
    reps = 0
    
Reset = Button(text="Reset",command = reset)
Reset.place(x=175,y=220)
 
#loop
window.mainloop()