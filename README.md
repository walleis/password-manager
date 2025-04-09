Py-ssword - Simple Password Manager

Py-ssword is a lightweight password manager built in Python using the Tkinter library. It allows users to generate secure random passwords, save login information (website, email/username, and password) to a text file, and copy generated passwords to the clipboard. The program includes basic validations to ensure fields are filled correctly and that the email has a valid format.

Features
Secure Password Generation: Generate random passwords with:
8 to 10 letters (uppercase and lowercase).
2 to 4 numbers.
2 to 4 symbols.
Clipboard Support: Automatically copies the generated password to the clipboard using pyperclip.
Field Validation: Ensures all fields are filled and the email contains @ and .com.
Password Storage: Saves login information to a passwords.txt file.
Dynamic Feedback: Displays labels to inform the user when a password is copied or saved.
User-Friendly Interface: Simple and intuitive design with Tkinter.

Prerequisites
Before running the program, ensure you have the following installed:

Python 3.x (recommended: Python 3.8 or higher)
Tkinter: Usually included with Python, but may need to be installed separately on some systems.
On Linux, install with: sudo apt-get install python3-tk

pyperclip: A Python library for copying text to the clipboard.
Install it using pip: pip install pyperclip

Standard Python Libraries:
random
string (used for password generation)

Installation
Clone the repository to your local machine: git clone https://github.com/walleis/password-manager.git

Navigate to the project directory: cd password-manager
Install the required dependency (pyperclip): pip install pyperclip

Ensure the logo.png file is present in the project directory. This file is used to display the logo in the interface. If you don’t have a logo.png file, create one or remove the reference to it in the code (lines related to the Canvas).
Run the program: python password_manager.py

Usage
Launch the Program:
Run the py-ssword.py script to open the graphical interface.

Fill in the Fields:
Website: Enter the website name (e.g., github.com).

Email/Username: Enter your email or username (e.g., user@example.com).

Password: Type a password manually or click "Generate Password" to create a random one.

Generate a Password:
Click the Generate Password button to create a random password.

The password will be:
Inserted into the password field.
Copied to your clipboard (using pyperclip).
A label will appear below the interface saying: "The random password got copied to your clipboard."

Save the Data:
Click the Add button to save the information.
The program checks if:
All fields are filled.
The email contains @ and .com.
If successful, the data is saved to passwords.txt in the format: 
Website: github.com | Email: user@example.com | Password: k9#mP$2vL!qR

