from tkinter import *
import math
from PIL import Image, ImageTk
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#ff817b"
ANOTHER_PINK = "#FF968A"
YELLOW_BG = "#FEE9C5"
BROWN = "#836953"
FONT_NAME = "Courier"
# CAN CHANGE FOR HOW LONG YOU WANT EACH TIMING TO BE
WORK_MIN = 60 # Can click "next" if finish work before 60 min
BREAK_MIN = 20 # Anime episode length without opening and ending songs (20)
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
    break_sec = BREAK_MIN * 60
    start_button.config(text="Next")
    
    if reps % 2 == 0:
        count_down(break_sec)
        title_label.config(text="Anime!", fg=BROWN)
        playsound("animedoro/sounds/erwin_sasageyo.mp3") # shinzo wo sasegayo
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=BROWN)
        playsound("animedoro/sounds/AlmightyPush.mp3") # Almighty Push

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
            marks += "🖥"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Animedoro Study Buddy :)")
window.config(padx=100, pady=50, bg=YELLOW_BG)

title_label = Label(text="Timer", fg=BROWN, bg=YELLOW_BG, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW_BG, highlightthickness=0)
image = Image.open("animedoro/pika.png") 
resized_image = image.resize((250, 275))
img = ImageTk.PhotoImage(resized_image)
canvas.create_image(100, 100, image=img)
timer_text = canvas.create_text(100, 210, text="00:00", fill=RED, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, fg=BROWN, font=(FONT_NAME, 20), width=5)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, fg=BROWN, font=(FONT_NAME, 20), width=5)
reset_button.grid(column=2, row=2)

check_marks = Label(bg=YELLOW_BG, font=(FONT_NAME, 25))
check_marks.grid(column=1, row=3)

window.mainloop()