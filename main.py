from math import floor
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
from config import FONT_NAME, YELLOW, GREEN, WORK_MIN, WORK_PERIODS, SHORT_BREAK_PERIODS, SHORT_BREAK_MIN, \
	LONG_BREAK_MIN

counter_is_on = False
reps = 0
check_mark_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_count():
	global counter_is_on
	global reps
	global check_mark_count
	
	reps = 0
	check_mark_count = 0
	
	if timer:
		window.after_cancel(timer)
		check_mark_label.config(text='')
		timer_label.config(text='TIMER')
		canvas.itemconfig(timer_text, text='00:00')
		counter_is_on = False

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
	global counter_is_on
	global reps
	global check_mark_count
	
	if not counter_is_on:
		
		reps += 1
		if reps in WORK_PERIODS:
			timer_label.config(text='WORK')
			check_mark_count += 1
			check_mark_label.config(text='✔' * check_mark_count)
			count_down(WORK_MIN * 60)
		elif reps in SHORT_BREAK_PERIODS:
			timer_label.config(text='SHORT BREAK')
			count_down(SHORT_BREAK_MIN * 60)
		else:
			timer_label.config(text='LONG BREAK')
			reps = 0
			check_mark_count = 0
			count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
	
	global counter_is_on
	global timer
	
	counter_is_on = True
	
	count_min = floor(count / 60)
	count_min = f'0{count_min}' if count_min < 10 else count_min
	
	count_sec = count % 60
	count_sec = f'0{count_sec}' if count_sec < 10 else count_sec
		
	canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
	
	if count > 0:
		timer = window.after(1000, count_down, count - 1)
	elif count == 0:
		counter_is_on = False
		start_timer()
		
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file='tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=2, column=2)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))

timer_label = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(row=1, column=2)

start_button = Button(text='START', bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=4, column=1)

reset_button = Button(text='RESET', bg=YELLOW, highlightthickness=0, command=reset_count)
reset_button.grid(row=4, column=3)

check_mark_label.grid(row=5, column=2)

window.mainloop()
