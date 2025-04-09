from random import shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import random

def random_password_generator():
    '''Function responsible for generating random passwords and copying to the clipboard.'''

    # List of characters.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Pick random characters from the list and stores in the variables.
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    # Put all the characters together.
    password_list = password_numbers + password_symbols + password_letters

    # Shuffle the characters.
    shuffle(password_list)

    # Put all the characters from the list into a single string.
    password = "".join(password_list)

    # Copy the password to the clipboard.
    pyperclip.copy(password)

    # Visual information to the user, so they know if the random password got copied.
    random_password_copied = Label(text="The random password got copied to your clipboard.")
    random_password_copied.grid(column=0, row=6, columnspan=2)

    # Fill the password field with the random generated password.
    password_entry.delete(0, END)
    password_entry.insert(0, string=f"{password}")


def save_password():
    '''Function responsible for saving the passwords, cleaning the entries and for showing errors.'''

    # Store the inputs.
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Detect empty fields and wrong emails.
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Empty fields detected", message="You need to fill the empty fields.")
    elif ".com" not in email or "@" not in email:
        messagebox.showerror(title="Invalid email", message="Your email must contain '@' and '.com'.")
    else:
        # Append the passwords to a .txt file.
        with open(f"./passwords.txt", mode="a") as passwords:
            passwords.write(f"Website: {website} | Email: {email} | Password: {password}\n")

        # Clear the values from the entries.
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

        # Visual information to the user, so they know if the password got saved.
        password_has_been_saved = Label(text="The password has been saved.")
        password_has_been_saved.grid(column=1, row=5)


# Window features.
window = Tk()
window.title("Py-ssword")
window.config(padx=50, pady=50) # Window size

# Canvas features.
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./logo.png")
canvas.create_image(60, 112, image=logo)
canvas.grid(column=1, row= 0)

# Labels.
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
user_website = website_entry.get()
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=1, sticky="w")
user_email = email_entry.get()

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")
user_password = password_entry.get()

# Buttons
generate_password_button = Button(text="Generate Password", command=random_password_generator)
generate_password_button.grid(column=1, row=3, sticky="e")

add_button = Button(text="Add", width=29, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()