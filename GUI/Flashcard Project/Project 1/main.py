from tkinter import *
import pandas as pd
import random

flip_timer = None
random_word = None

#TODO: ------------------------------- NEXT WORD --------------------------------------------
# Try to read words_to_learn.csv file. If file not found, then read data.csv file.
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/data.csv")
finally:
    data_dict = data.to_dict(orient="records")
    # set orient = records to follow this formating: {english: word, vietnamese: word}.
    # ‘records’ : make list like [{column -> value}, … , {column -> value}]

def next_card():
    """Showing random a English word on canvas."""

    global flip_timer, random_word
    window.after_cancel(flip_timer)

    random_word = random.choice(data_dict)

    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"].title(), fill="white")

    flip_timer = window.after(2000, flip, random_word)
 
def flip(random_word):
    """Flip the canvas and convert to Vietnamese."""

    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="Vietnamese", fill="black")
    canvas.itemconfig(card_word, text=random_word["Vietnamese"].title(), fill="black")
    
def is_known():
    """Remove the known-words. """

    data_dict.remove(random_word)
    to_learn = pd.DataFrame(data_dict)  
    to_learn.to_csv("data/words_to_learn.csv", index=False) # index=False : remove index.
    next_card()

#TODO: -------------------------------- UI SETUP --------------------------------------------
# Create the window.
window = Tk()
window.title("Flashy")
window.config(bg="white", padx=50, pady=50)

# Create a canvas.
canvas = Canvas(width=687, height=363)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(343, 170, image=card_front_img)
card_title = canvas.create_text(343, 80, text="", font=("Ariel", 30, "italic"), fill="white")
card_word = canvas.create_text(343, 200, text="", font=("Ariel", 40, "bold"), fill="white")
canvas.config(bg="white", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons with icon image.
known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img, highlightthickness=0, bg="white", activebackground="white",
                                                            relief="flat", command=is_known)
known_button.grid(row=1, column=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, bg="white", activebackground="white",
                                                            relief="flat", command=next_card)
unknown_button.grid(row=1, column=0)

flip_timer = window.after(3000, flip, random_word)
next_card()


window.mainloop()