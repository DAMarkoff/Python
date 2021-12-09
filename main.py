from random import randint, choice, shuffle
from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END, messagebox
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
	password_entry.delete(0, END)
	
	password_list = [choice(letters) for _ in range(randint(8, 10))]
	password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
	password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
	
	shuffle(password_list)
	
	password = "".join(password_list)
	password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
	website = website_entry.get()
	user = user_entry.get()
	password = password_entry.get()
	data_to_save = {
		website: {
			'user': user,
			'password': password
		}
	}
	if website and user and password:
		answer = messagebox.askokcancel(message=f'Details: \nWebsite: {website} \nEmail: {user} \nPassword: {password} '
		                                        f'\n\nSave to file?', parent=window)
		if answer:
			try:
				with open('data.json', 'r') as file:
					try:
						json_data = json.load(file)
					except json.decoder.JSONDecodeError:
						json_data = {}
					json_data.update(data_to_save)
			except FileNotFoundError:
				with open('data.json', 'w') as file:
					json_data = data_to_save
			finally:
				with open('data.json', 'w') as file:
					json.dump(json_data, file, indent=4)
				website_entry.delete(0, END)
				password_entry.delete(0, END)
				messagebox.showinfo(message='Data has been added', parent=window, icon='info')
	else:
		messagebox.showwarning(message='Please, provide data needed', parent=window)

# ---------------------------- SHOW PASSWORD ------------------------------- #


def search_password():
	website = website_entry.get()
	if website:
		try:
			with open('data.json', 'r') as file:
				json_data = json.load(file)
		except FileNotFoundError:
			messagebox.showwarning(message='File not found', parent=window)
		else:
			if website in json_data:
				user = json_data[website]['user']
				password = json_data[website]['password']
				messagebox.showinfo(message=f'Website: {website}\nEmail: {user}\nPassword: {password}', parent=window,
				                    icon='info')
			else:
				messagebox.showwarning(message=f'{website} data not found', parent=window)
	else:
		messagebox.showwarning(message='Please, provide data needed', parent=window)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_entry = Entry(width=38)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'email@domain.com')

password_entry = Entry(width=21, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text='Search', width=13, command=search_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text='Generate password', command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add password', width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
