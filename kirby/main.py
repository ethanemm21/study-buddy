from tkinter import *
import math
from PIL import Image, ImageTk
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
ANOTHER_PINK = "#FF968A"
YELLOW = "#f7f5dd"
PINK_BG = "#F9C5D5"
BUTTON_FGCOLOR = "#F2789F"
FONT_NAME = "Courier"
# CAN CHANGE FOR HOW LONG YOU WANT EACH TIMING TO BE
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        playsound("kirby/sounds/sound2.mp3")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        playsound("kirby/sounds/sound2.mp3")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=ANOTHER_PINK)
        playsound("kirby/sounds/sound1.mp3")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "🐶"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Study Buddy :)")
window.config(padx=100, pady=50, bg=PINK_BG)

title_label = Label(text="Timer", fg=ANOTHER_PINK, bg=PINK_BG, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=PINK_BG, highlightthickness=0)
image = Image.open("kirby/kirby.png")
resized_image = image.resize((150, 175))
img = ImageTk.PhotoImage(resized_image)
canvas.create_image(100, 100, image=img)
timer_text = canvas.create_text(100, 210, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, fg=BUTTON_FGCOLOR, font=(FONT_NAME, 20))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, fg=BUTTON_FGCOLOR, font=(FONT_NAME, 20))
reset_button.grid(column=2, row=2)

check_marks = Label(fg=ANOTHER_PINK, bg=PINK_BG, font=(FONT_NAME, 25))
check_marks.grid(column=1, row=3)

window.mainloop()