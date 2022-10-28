from tkinter import *
import random

FONT_NAME = "Arial"

EVERYTHING = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
           ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_entry():
    saved_email = email_text.get()
    saved_website = website_text.get()
    saved_password = password_text.get()
    with open("passwords.txt", mode="a") as file:
        file.write(f"\n{saved_website} | {saved_email} | {saved_password}")

def generate_pw():
    new_password = ""
    for iterator in range(0,12):
        entry = random.choice(EVERYTHING)
        new_password += entry
    password_text.delete(0, END)
    password_text.insert(0, new_password)






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
website_text = Entry(width=35)
website_text.grid(column=1, row=1, columnspan=2)

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

website_text.focus()


window.mainloop()
