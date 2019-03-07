# Password Generator App

"""
Write a password generator in Python.
Strong Passwords have a mix of lowercase letters, uppercase letters, numbers and symbols.
Password should be random generating a new password every time the user asks for a new password.
Include your run time code in a main method.

Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

from random import *
from string import *

print("----------------------")
print("PASSWORD GENERATOR APP")
print("----------------------")

password_db = []

new_password_request = input("Do you want to generate a new password? (Y/N): ")

def main(new_password_request):

    if new_password_request == 'Y' or new_password_request == 'y':
        password_strength = int(input("Choose the password strength: 1. Weak, 2. Medium, 3. Strong. : "))

        if password_strength == 1:
            size = 8
            choice = sample(ascii_letters, size)
            password = ''.join(choice)
            print("The new generated password: ", password)
            password_db.append(password)
        elif password_strength == 2:
            size = 16
            combined = ascii_letters + punctuation
            choice = sample(combined, size)
            password = ''.join(choice)
            print("The new generated password: ", password)
            password_db.append(password)
        elif password_strength == 3:
            size = 24
            combined = ascii_letters + punctuation + digits
            choice = sample(combined, size)
            password = ''.join(choice)
            print("The new generated password: ", password)
            password_db.append(password)
        else:
            print("Invalid choice. Please enter choice for Password Strength between 1 to 3")
            
    elif new_password_request == 'N' or new_password_request == 'n':
        print("Thank you for using Password Generator App")

    else:
        print("Invalid choice.") 

main(new_password_request)
