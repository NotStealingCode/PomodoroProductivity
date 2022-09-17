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
new_checkmark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    text_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    my_label.config(text="", font=(FONT_NAME, 12, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        text_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        text_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
        count_down(short_break_sec)
    else:
        text_label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global new_checkmark
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
        if reps % 2 == 0:
            new_checkmark += "✔"
            my_label.config(text=new_checkmark, font=(FONT_NAME, 12, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.resizable(width=None, height=None)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
text_label.config(fg=GREEN, bg=YELLOW)
text_label.grid(column=1, row=0)

my_label = Label(font=(FONT_NAME, 12, "bold"))
my_label.config(fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 16, "normal"), highlightthickness=0, bg=YELLOW,
                      command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=(FONT_NAME, 16, "normal"), highlightthickness=0, bg=YELLOW,
                      command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
