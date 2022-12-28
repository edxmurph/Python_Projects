# Password Manager

from tkinter import *
import tkinter.messagebox as mb
import random
import json
import string
import pyperclip

FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 10)
DEFAULT_USERNAME = "dungnguyentuan95@gmail.com"
# characters to use in generated passwords
LETTERS = string.ascii_letters     # a string containing all ASCII letters.
NUMBERS = string.digits            # a string containing all ASCII decimal digits.
# SYMBOLS = string.punctuation     # a string containing all ASCII punctuation characters.
# This also works as well but not included :;'"\|/... 
SYMBOLS = "!@#$%^&*()-_=+[{}]<>?" 
DATA_FILE = "data.json"


def generate_password():
    """Generates a password matching the parameters and copies it to the clipboard."""
    # using list comprehension for practice
    letters = [let for let in LETTERS]
    numbers = [num for num in NUMBERS]
    symbols = [sym for sym in SYMBOLS]

    password_list = []

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    # need to use a special tkinter identifier END when clearing the field
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # clear the clipboard and copy the value
    pyperclip.copy(password)


def add_info():
    """Checks the validity of the provided values and saves them into the file."""
    # Get data from user's input.
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email/phone": email,
            "password": password
        }
    }

    # Warning if there's empty fields.
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        mb.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        # ask for confirmation
        is_ok = mb.askokcancel(title=website, message=f"Please confirm the following are correct:\n\n"
                                                      f"Email/Username: {email}\n"
                                                      f"Password: {password}\n\n"
                                                      f"Save infomation?")
        # If it's ok then save the data to data.json.
        if is_ok:
            try:
                # Try to open data.json file.
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                # If there's no data.json file, then create it and add the new data.
                with open("data.json", "w") as data_file:    
                    json.dump(new_data, data_file, indent=4)
            else:
                # If there already is data.json file, then update the new data.
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:    
                # Clear the previous entry in order to save the new one.
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                #Taking the cursor to website's entry.
                website_entry.focus()
            

def search():
    """Searches the data for an entry matching the string in the "Website" field."""
    # Get the website.
    website = website_entry.get().title()

    # Get hold of the data and showing in messagebox.
    try:
        # Try to get data's website from data.json.
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            confirm_copy = mb.askyesno(title=website, message=f"Email/Phone: {data[website]['email/phone']}\n"
                                                              f"Password: {data[website]['password']}\n\n"
                                                              f"Do you want to copy password to your clipboard?")
    except KeyError:
        # If there's no that website, then show the error message.
        mb.showerror(title="Oops.", message="No details for the website exists.")
    except FileNotFoundError:
        # If there's no data.json file, then show the error message.
        mb.showerror(title="Oops.", message="No data file found.")
    else:
        # Copy password to the clipboard.
        if confirm_copy:
            pyperclip.copy(data[website]['password'])


# main window setup
root = Tk()
root.title("Password Manager")
root.iconbitmap("icon.ico")
root.geometry("550x400")
root.resizable(False, False)

# top frame
top_frame = Frame(root)
top_frame.pack()
# canvas
canvas = Canvas(top_frame, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# the top frame only has a single element, so a simple pack() works just fine
canvas.pack(padx=20, pady=20)

# bottom frame
bottom_frame = Frame(root)
bottom_frame.pack()
# left column
website_label = Label(bottom_frame, text="Website:", font=FONT, width=16)
website_label.grid(row=0, column=0, pady=4)
email_label = Label(bottom_frame, text="Email/Username:", font=FONT, width=16)
email_label.grid(row=1, column=0, pady=4)
password_label = Label(bottom_frame, text="Password:", font=FONT, width=16)
password_label.grid(row=2, column=0, pady=4)

# middle+right column
email_entry = Entry(bottom_frame, font=FONT, width=31)
email_entry.grid(row=1, column=1, columnspan=2, pady=4)
email_entry.insert(0, DEFAULT_USERNAME)
add_button = Button(bottom_frame, text="Add", font=BUTTON_FONT, bg="#ddd", width=32,
                                                        relief="groove", command=add_info)
add_button.grid(row=3, column=1, columnspan=2, pady=8)

# middle column
website_entry = Entry(bottom_frame, font=FONT, width=18)
website_entry.grid(row=0, column=1, padx=8, pady=4)
website_entry.focus()
password_entry = Entry(bottom_frame, font=FONT, width=18)
password_entry.grid(row=2, column=1, padx=8, pady=4)

# right column
search_button = Button(bottom_frame, text="Search", font=BUTTON_FONT, width=15,
                                                        relief="groove", command=search)
search_button.grid(row=0, column=2, padx=7, pady=4)
password_button = Button(bottom_frame, text="Generate Password", font=BUTTON_FONT, width=15,
                                                        relief="groove", command=generate_password)
password_button.grid(row=2, column=2, padx=7, pady=4)

# main loop
root.mainloop()
