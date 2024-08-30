from tkinter import *

from pandas.core.window import Window
from pandas.io.sas.sas_constants import column_label_length_length

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg= YELLOW)
canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130, text= "00:00", fill="white", font=(FONT_NAME,34, "bold"))
label = Label( text= "Timer", font=(FONT_NAME,34, "bold"), fg=GREEN, bg= YELLOW)
label_check = Label( text= "✔", font=(FONT_NAME,24, "bold"), fg=GREEN, bg= YELLOW)
button_start = Button(text="Start", highlightthickness=0)
button_start.grid(column=0,row=3)
button_reset = Button(text="Reset", highlightthickness=0)
button_reset.grid(column=3,row=3)
label.grid(column=1,row=0)
canvas.grid(column=1,row=2)
label_check.grid(column=1,row=3)



window.mainloop()