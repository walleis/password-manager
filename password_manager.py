from random import shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Detect empty fields and wrong emails.
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Empty fields detected", message="You need to fill the empty fields.")
    elif ".com" not in email or "@" not in email:
        messagebox.showerror(title="Invalid email", message="Your email must contain '@' and '.com'.")
    else:
        try:
            # Try to open and read the passwords from passwords.json
            with open("./passwords.json", mode="r") as data_file:
                data = json.load(data_file) # Read the existing data
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty/invalid, start with an empty dictionary
            with open("./passwords.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update the data with the new entry
            data.update(new_data)
            # Write the updated data back to the file
            with open("./passwords.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4) # Save updated data
        finally:
            # Clear the values from the entries.
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

        # Visual information to the user, so they know if the password got saved.
        password_has_been_saved = Label(text="The password has been saved.")
        password_has_been_saved.grid(column=1, row=5)

def find_password():
    '''Function responsible for finding an existing password.'''

    # Store the inputs.
    website = website_entry.get()
    try:
        with open("./passwords.json", mode="r") as data_file:
            data = json.load(data_file)  # Read the existing data
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Password found!", message=f"{website}\nEmail: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} found.")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"No password file found.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Error reading password file.")

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

search_button = Button(text="           Search           ", command=find_password)
search_button.grid(column=1, row=1, sticky="e")

add_button = Button(text="Add", width=29, command=find_password)
add_button.grid(column=1, row=4, columnspan=2)

# Keeps the window open.
window.mainloop()
