from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_FRENCH_WORD = ""

# -------------------------- CSV SETUP --------------------------- #

try:
    fr_en_data = pandas.read_csv("./data/words_to_learn.csv")
    fr_en_dict = {row.French: row.English for (index, row) in fr_en_data.iterrows()}
except FileNotFoundError:
    fr_en_data = pandas.read_csv("./data/french_words.csv")
    print(fr_en_data)
    fr_en_dict = {row.French: row.English for (index, row) in fr_en_data.iterrows()}
    print(fr_en_dict)
finally:
    french_words = [french for (french, english) in fr_en_dict.items()]
    english_words = [english for (french, english) in fr_en_dict.items()]

# --------------------------SCREEN FUNCTION ---------------------- #


def new_card():

    global CURRENT_FRENCH_WORD, FLIP_TIME
    window.after_cancel(FLIP_TIME)
    CURRENT_FRENCH_WORD = ""

    try:
        random_fr = random.choice(french_words)
    except IndexError:
        messagebox.showinfo(title="Completed the flash cards",
                            message="You have finished the entire flash card list!")
    else:
        CURRENT_FRENCH_WORD = random_fr

        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(definition_word, text=random_fr, fill="black")

        FLIP_TIME = window.after(3000, flip_card)


def flip_card():

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(definition_word, text=fr_en_dict[CURRENT_FRENCH_WORD], fill="white")


def correct():

    global CURRENT_FRENCH_WORD

    try:
        french_words.remove(CURRENT_FRENCH_WORD)

    except ValueError:
        messagebox.showinfo(title="Completed the flash cards",
                            message="You have finished the entire flash card list!")

    else:
        english_words.remove(fr_en_dict[CURRENT_FRENCH_WORD])

        new_dict = {
            "French": french_words,
            "English": english_words,
        }

        df_new_dict = pandas.DataFrame(new_dict)
        df_new_dict.to_csv("./data/words_to_learn.csv", index=False)

        new_card()

# -------------------------- UI SETUP ---------------------------- #


window = Tk()
window.title("Flashcard Application")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

FLIP_TIME = window.after(3000, flip_card)

# Images
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=525, highlightthickness=0)
canvas_image = canvas.create_image(400, 262, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Texts
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
definition_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Buttons
correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct)
correct_button.grid(row=1, column=1)
incorrect_button = Button(image=incorrect_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_card)
incorrect_button.grid(row=1, column=0)

new_card()

window.mainloop()
