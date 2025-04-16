# Py-ssword - Password Generator and Manager

## Description

Py-ssword is a simple and intuitive application developed in Python using the Tkinter library to generate strong random passwords and securely manage your website credentials. It allows you to save your websites, emails/usernames, and passwords in a local JSON file, as well as offering the functionality to generate complex passwords with a single click and copy them to the clipboard.

## Features

* **Strong Password Generation:** Creates random passwords by combining uppercase and lowercase letters, numbers, and symbols.
* **Clipboard Copy:** Automatically copies the generated password so you can easily paste it.
* **Credential Saving:** Allows you to save the website, email/username, and associated password.
* **Secure Storage:** Credentials are stored locally in a `passwords.json` file.
* **Password Search:** Facilitates searching for saved passwords by website name.
* **User-Friendly Graphical Interface:** Utilizes the Tkinter library for a simple and direct user experience.

## How to Use

1.  **Run the script:** Make sure you have Python installed on your system. Save the code as a `.py` file (e.g., `py_ssword.py`) and run it through the terminal or by double-clicking the file.
2.  **Main Interface:** The main Py-ssword window will appear with fields for "Website:", "Email/Username:", and "Password:".
3.  **Generate Password:**
    * Click the "Generate Password" button to create a random and complex password.
    * The generated password will be automatically copied to your clipboard and displayed in the "Password:" field. A confirmation message will appear.
4.  **Save Password:**
    * Fill in the "Website:", "Email/Username:", and optionally edit the generated password in the "Password:" field.
    * Click the "Add" button to save the information. A confirmation message will indicate that the password has been saved.
5.  **Search Password:**
    * Enter the website name in the "Website:" field.
    * Click the "Search" button.
    * If the password for the entered website is found, a pop-up window will display the website, email, and corresponding password.
    * If the website is not found, an error message will be displayed.

## Requirements

* Python 3.x
* Python Libraries:
    * `random` (installed with Python)
    * `tkinter` (installed with Python on most systems)
    * `pyperclip` (can be installed via pip: `pip install pyperclip`)

## Installation

1.  Ensure you have Python installed on your system.
2.  Install the `pyperclip` library if it's not already installed:
    ```bash
    pip install pyperclip
    ```
3.  Save the provided Python code in a file named `py_ssword.py` (or any other name you prefer).
4.  Run the `py_ssword.py` script.

## File Structure

* `py_ssword.py`: The main file containing the application code.
* `logo.png`: An optional logo image (the script assumes this file is in the same directory).
* `passwords.json`: A JSON file created to store the saved credentials. This file will be automatically created the first time you save a password.

## Security Notes

* Passwords are stored locally in an unencrypted JSON file. For enhanced security, consider using dedicated password management solutions with robust encryption.
* Be cautious when sharing the `passwords.json` file, as it contains your login information.
