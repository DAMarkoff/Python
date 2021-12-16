from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
dictionary = []
random_word = {}


def words_to_learn_from_french_words():
	global dictionary
	data = pandas.read_csv('data/french_words.csv')
	data.to_csv('data/words_to_learn.csv', index=False)
	dictionary = data.to_dict(orient="records")


def open_words_to_learn():
	global dictionary
	try:
		data = pandas.read_csv('data/words_to_learn.csv')
		dictionary = data.to_dict(orient="records")
	except FileNotFoundError:
		words_to_learn_from_french_words()


def next_card():
	global random_word, flip_timer
	window.after_cancel(flip_timer)
	random_word = random.choice(dictionary)
	canvas.itemconfig(canvas_image, image=card_front)
	canvas.itemconfig(card_title, text='French', fill='black')
	canvas.itemconfig(card_word, text=random_word['French'], fill='black')
	flip_timer = window.after(3000, func=flip_card)


def flip_card():
	canvas.itemconfig(canvas_image, image=card_back)
	canvas.itemconfig(card_title, text='English', fill='white')
	canvas.itemconfig(card_word, text=random_word['English'], fill='white')


def green_button():
	global dictionary
	dictionary.remove(random_word)
	if len(dictionary) == 0:
		messagebox.showinfo(message='Start from the very beginning', parent=window, icon='info')
		words_to_learn_from_french_words()
	df = pandas.DataFrame(dictionary)
	df.to_csv('data/words_to_learn.csv', index=False)
	next_card()
	
	
window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
canvas_image = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='English', font=('Arial', 60, 'bold'))

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=green_button)
right_button.grid(row=1, column=1)

open_words_to_learn()
next_card()

window.mainloop()
