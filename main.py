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
rep = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)

def start_count():
    global rep
    if rep > 8:
        rep = 1
    if rep in [1,3,5,7]:
        counter(25*60)
        label1.config(text="Work Time", fg=GREEN)
    elif rep in [2,4,6]:
        counter(5*60)
        label1.config(text="Break Time", fg=RED)
        if rep == 2:
            tick_label.config(text="✔", bg=YELLOW, fg=GREEN)
        elif rep == 4:
            tick_label.config(text="✔✔", bg=YELLOW, fg=GREEN)
        elif rep == 6:
            tick_label.config(text="✔✔✔", bg=YELLOW, fg=GREEN)
    elif rep == 8:
        counter(20*60)
        label1.config(text="Long Break Time", fg=PINK)
        tick_label.config(text="✔✔✔✔", bg=YELLOW, fg=GREEN)

def counter(count=0, reset = False):
    global rep, timer
    if reset:
        window.after_cancel(timer)
    else:
        count_min = int(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = '0' + str(count_sec)
        if count_min < 10:
            count_min = '0' + str(count_min)
        timer = canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            window.after(1000, counter, count-1)
        else:
            rep += 1
            start_count()

def reset():
    global rep, timer
    counter(reset=True)
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text=" ", bg=YELLOW, fg=GREEN)
    rep = 0



label1 = Label(text="Timer", font=("Georgia", 40, 'bold'), bg=YELLOW, fg=GREEN)
label1.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_t = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_t)
timer_text = canvas.create_text(100, 130, fill="white", font=(FONT_NAME, 35, 'bold'), text='00:00')
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_count)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

tick_label = Label(text=" ", bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=1)


window.mainloop()