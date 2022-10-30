from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


FONT_NAME = "Arial"

EVERYTHING = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
           ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    new_password = ""
    for iterator in range(0,12):
        entry = random.choice(EVERYTHING)
        new_password += entry
    password_text.delete(0, END)
    password_text.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_entry():
    saved_email = email_text.get()
    saved_website = website_text.get()
    saved_password = password_text.get()
    if saved_website == "" or saved_email == "" or saved_password == "":
        messagebox.showwarning("Missing Information", "Please enter all information before saving!")

    elif messagebox.askyesno("Confirmation", f"Website: {saved_website}\nEmail: {saved_email}\nPassword: "
                                             f"{saved_password}\nIs this correct?"):

        json_data = {
            saved_website: {
                "email": saved_email,
                "password": saved_password,
            }
        }

        try:
            with open("password_data.json", mode="r") as file:
                json_saved = json.load(file)
                json_saved.update(json_data)
        except FileNotFoundError as e:
            with open("password_data.json", mode="a") as file:
                json.dump(json_data, file, indent=4)

        else:
            with open("password_data.json", mode="w") as file:
                json.dump(json_saved, file, indent=4)

        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)

# ------------------------- SEARCH WEBSITE ---------------------------- #

def search_website():
    try:
        with open("password_data.json", mode="r") as file:
            json_reader = json.load(file)
            site_search_kw = website_text.get()
    except FileNotFoundError as e:
        messagebox.showwarning(title="File Not Found", message="Please add an entry before searching")

    else:
        try:
            messagebox.showinfo(title="Result", message=f"Website: {site_search_kw}\nEmail: "
                                                        f"{json_reader[site_search_kw]['email']}\nPassword: "
                                                        f"{json_reader[site_search_kw]['password']}")
        except KeyError as e:
            messagebox.showwarning(title="Wrong Input", message="Input in 'website' field was not found in file")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
my_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image((100, 100), image=my_img)
canvas.grid(column=1, row=0)


# labels

site_label = Label(text="Website :", font=(FONT_NAME, 10))
site_label.grid(column=0, row=1)

email_label = Label(text="Email/Username :", font=(FONT_NAME, 10))
email_label.grid(column=0, row=2)

password_label = Label(text="Password :", font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

# text fields
website_text = Entry(width=19)
website_text.grid(column=1, row=1)

email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, "jamjam.perey@gmail.com")

password_text = Entry(width=19)
password_text.grid(column=1, row=3)

# buttons

gen_pw_btn = Button(text="Generate Password", highlightthickness=0, width=12, command=generate_pw)
gen_pw_btn.grid(column=2, row=3)

add_btn = Button(text="Add", highlightthickness=0, width=33, command=add_entry)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", highlightthickness=0, width=12, command= search_website)
search_btn.grid(column=2, row=1)


website_text.focus()


window.mainloop()
