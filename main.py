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
check_icon = ""
timer = None

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("+1+1")

# Labels
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


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

    if count_min == 0 and int(count_sec) == 0:
        start_timer()


def start_timer():
    global reps
    global check_icon
    if reps > 0 and reps % 2 == 0:
        check_icon += "✔"
    checkmark.config(text=check_icon)

    reps += 1

    if reps in [1, 3, 5, 7]:
        count_down(WORK_MIN * 60)
        # count_down(10)  ## Stubs for faster testing
        title_label.config(text="Work", fg=GREEN)

    elif reps in [2, 4, 6]:
        count_down(SHORT_BREAK_MIN * 60)
        # count_down(5)  ## Stubs for faster testing
        title_label.config(text="Break", fg=PINK)

    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        # count_down(20)  ## Stubs for faster testing
        title_label.config(text="Break", fg=RED)


def reset_timer():
    global timer
    global timer_text
    global check_icon
    global checkmark
    global reps
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label = "Timer
    title_label.config(text="Timer")
    # reset check_marks
    check_icon = ""
    checkmark.config(text=check_icon)
    reps = 0


start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)


window.mainloop()
