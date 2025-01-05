from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CREAM = "#ede8b2"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
SMALL_FONT = (FONT_NAME, 10, "bold")
reps = 0
check = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        reset_timer()
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        window.attributes("-topmost", True)
        window.focus_force()

        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += check
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", borderwidth=0, font=SMALL_FONT, bg=CREAM, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", borderwidth=0, font=SMALL_FONT, bg=CREAM, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
