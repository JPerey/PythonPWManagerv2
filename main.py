from tkinter import *


FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
my_img = PhotoImage(file="logo.png")

canvas = Canvas(width=240, height=240, highlightthickness=0)
canvas.create_image((120, 120), image=my_img)
canvas.grid(column=1, row=0)


# labels

site_label = Label(text="Website :", font=(FONT_NAME, 12))
site_label.grid(column=0, row=1)

email_label = Label(text="Email/Username :", font=(FONT_NAME, 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password :", font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

# text fields
website_text = Text(width=46, height= 1)
website_text.grid(column=1, row=1, columnspan=2)

email_text = Text(width=46, height=1)
email_text.grid(column=1, row=2, columnspan=2)

password_text = Text(width=28, height=1)
password_text.grid(column=1, row=3)

# buttons

gen_pw_btn = Button(text="Generate Password", highlightthickness=0, width=10)
gen_pw_btn.grid(column=2, row=3)

add_btn = Button(text="Add", highlightthickness=0, width=36)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
