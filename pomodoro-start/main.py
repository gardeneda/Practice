from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK_SINGLE = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    global REPS

    REPS = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global REPS

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 7 == 0 and REPS != 0:
        timer_label.config(fg=RED, text="Long Break")
        count_down(long_break_sec)

    elif REPS % 2 == 0:
        timer_label.config(fg=GREEN, text="Work")
        count_down(work_sec)
        # if REPS != 0:
        #     total_checks += CHECK_SINGLE
        # checkmark_label.config(text=total_checks)

        total_checks = ""  # Why couldn't you think of doing this inside? You are too accustomed to working in one way.
        for _ in range(REPS//2):
            total_checks += CHECK_SINGLE
        checkmark_label.config(text=total_checks)

    elif REPS % 2 != 0:
        timer_label.config(fg=PINK, text="Break")
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    global REPS

    count_min = count // 60
    count_min_format = "{:02d}".format(count_min)
    count_sec = count % 60
    count_sec_format = "{:02d}".format(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min_format}:{count_sec_format}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        REPS += 1
        start_timer()  # You can call a function within another function, you seem to keep forgetting this.


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
TOMATO_IMG = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=TOMATO_IMG)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)  # Change this to grid (change the entire UI program to grid())


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
checkmark_label.grid(column=2, row=4)

# Using fg, you will be able to color labels in TKinter.
# You can also copy symbols (i.e. ✔) from the internet to use as your label. (You can also color them)


# ROW 0     0  1  2  3  4
# ROW 1     0  1  2  3  4
# ROW 2     0  1  2  3  4
# ROW 3     0  1  2  3  4
# ROW 4     0  1  2  3  4

window.mainloop()
