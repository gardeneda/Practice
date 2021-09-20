import tkinter as gui
import pyperclip
from tkinter import messagebox
# Although you imported all of the tkinter class on the line above, (Classes and Constants)
# It doesn't import the 'messagebox' module, because its just another module of code.
# In fact, if you right click on it and move into the implementation, you are able to see the file.

import string
import random
import json
from json import JSONDecodeError
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():

    # characters = [n for n in string.ascii_letters]
    # symbols = [n for n in string.punctuation]
    # numbers = [n for n in string.digits]

    # There's going to be a character limit to this.
    password_entry.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_final = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password_final)
    pyperclip.copy(password_final)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_name = website_entry.get()
    website = website_name.upper()
    user_id = user_id_entry.get()
    password = password_entry.get()

    if not website_name or not user_id or not password:
        messagebox.showwarning(title="Oops!", message="Please do not leave any fields empty!")
        return None

    # is_ok = messagebox.askokcancel(title=website_name,
    #                                message=f"These are the details entered: \n\n\n"
    #                                f"Website: {website_name}\n"
    #                                f"User: {user_id}\n"
    #                                f"Password: {password}\n\n\n"
    #                                f"Is it okay to save?")
    #
    # if is_ok:
    #     with open("./Manager.txt", mode="a") as file:
    #         file.write(f"Website: {website_name} | id: {user_id} | Password: {password}\n")
    #
    #     website_entry.delete(0, "end")
    #     password_entry.delete(0, "end")

# ------- USING JSON TO DO THE ABOVE ---------------------------------- #

    new_data = {
        website: {
            "email": user_id,
            "password": password,
        }
    }

    try:
        with open("./Manager.json", mode="r") as y_file:  # Take good notice that the mode is "r"
            # Reading old data
            data = json.load(y_file)

    except FileNotFoundError or JSONDecodeError:
        with open("./Manager.json", mode="w") as y_file:
            json.dump(new_data, y_file, indent=4)

    else:
        # Updating old data with new data
        data.update(new_data)

        # Saving updated data
        with open("./Manager.json", mode="w") as y_file:
            json.dump(data, y_file, indent=4)

    finally:
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")

# --------------------------SEARCH FUNCTION ----------------------------#


def search_duplicate():

    website_name = website_entry.get()
    website = website_name.upper()

    try:
        with open("./Manager.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError or JSONDecodeError:
        messagebox.showwarning(title="No Registries",
                               message="You do not have any accounts entered into the database.")
        return None

    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website_name}", message=f"Username:  {username}\n"
                                                                 f"Password:  {password}")
        else:
            messagebox.showwarning(title="Not registered.",
                                   message="No searches were found for this website/company.")


# Prioritize the usage of the "if, else" statement, then to rely on the try, except error.
# Only use the exception handling when you cannot easily do it with an if/else statement.


# ---------------------------- UI SETUP ------------------------------- #

window = gui.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = gui.Canvas(width=200, height=200)
LOCK_IMAGE = gui.PhotoImage(file="./logo.png")
canvas.create_image(113, 100, image=LOCK_IMAGE)
canvas.grid(row=0, column=1, sticky="n")

website_label = gui.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
website_entry = gui.Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="n")

user_id_label = gui.Label(text="Email/Username:")
user_id_label.grid(row=2, column=0, sticky="n")
user_id_entry = gui.Entry(width=52)
# user_id_entry.insert(0, CONSTANT_ID)
user_id_entry.grid(columnspan=2, row=2, column=1, sticky="n")

password_label = gui.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")
password_entry = gui.Entry(width=33)
password_entry.grid(row=3, column=1, sticky="e")


# Buttons
generate_button = gui.Button(text="Generate Password", command=create_password, width=15)
generate_button.grid(row=3, column=2, sticky="e")

add_button = gui.Button(text="Add",width=44, command=save)
add_button.grid(columnspan=2, row=4, column=1, sticky="e")

search_button = gui.Button(text="Search", width=15, command=search_duplicate)
search_button.grid(row=1, column=2)

window.mainloop()
