import tkinter
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthicknes=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text='Start', highlightthicknes=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', highlightthicknes=0)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text='✅', bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
