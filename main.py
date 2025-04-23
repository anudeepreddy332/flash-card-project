import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import  pandas as pd

current_card = {}
french_words_dictionary = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    french_words_dictionary = original_data.to_dict(orient="records")
else:
    french_words_dictionary = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_words_dictionary)
    my_canvas.itemconfig(card_image,image=card_front_img)
    my_canvas.itemconfig(card_title,text="French",fill="black")
    my_canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    my_canvas.itemconfig(card_image,image=card_back_img)
    my_canvas.itemconfig(card_title,text="English",fill="white")
    my_canvas.itemconfig(card_word,text=current_card["English"],fill="white")

def is_known():
    french_words_dictionary.remove(current_card)
    data = pd.DataFrame(french_words_dictionary)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, flip_card)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

my_canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_image = my_canvas.create_image(400,263, image=card_front_img)
card_title = my_canvas.create_text(400,150,text="",font=("Arial",40,"italic"),fill="black")
card_word = my_canvas.create_text(400,263,text="",font=("Arial",60,"bold"),fill="black")

my_canvas.grid(row=0,column=0,columnspan=2)

right_button = Button(image=right_img,highlightthickness=0,border=0,
                      borderwidth=0,bg=BACKGROUND_COLOR,command=is_known)
right_button.grid(row=1,column=1)
wrong_button = Button(image=wrong_img,highlightthickness=0,
                      border=0,borderwidth=0,bg=BACKGROUND_COLOR,command=next_card)
wrong_button.grid(row=1,column=0)


next_card()














window.mainloop()