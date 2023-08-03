import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

finally:
    to_learn = data.to_dict(orient="records")
    current_card = {}


def generate_new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    datas = pandas.DataFrame(to_learn)
    datas.to_csv("data/words_to_learn.csv", index=False)
    generate_new_card()

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_new_card)
wrong_button.grid(column=0, row=1)

generate_new_card()

window.mainloop()
# We can add many languages and words from https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Frequency_lists
