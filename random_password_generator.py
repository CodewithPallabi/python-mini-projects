''' creating a password generator that will pick characters from available characters(upper case, lower case, digits, special characters)
It should contain atleast one of each character type.
'''

import random
import string

def password_generator():
    while True:
        try:
            length = int(input("Enter the password length: ").strip())
            break
        except ValueError:
            print("Enter a valid number...")

    
    # if length < 5:
    #     print("password length must be contain atleast 5 charaters.")
    #     return
        
    include_uppercase = input("Do you wanna include uppercase letters? (y/n): ").lower().strip()
    include_lowercase = input("Do you wanna include lowercase letters? (y/n): ").lower().strip()
    include_digits = input("Do you wanna include digits? (y/n): ").lower().strip()
    include_special = input("Do you wanna include special characters? (y/n): ").lower().strip()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    all_characters = upper + lower + digits + special

    required_charecters = []
    if include_uppercase == "y":
        required_charecters.append(random.choice(upper))
    if include_lowercase == "y":
        required_charecters.append(random.choice(lower))
    if include_digits == "y":
        required_charecters.append(random.choice(digits))
    if include_special == "y":
        required_charecters.append(random.choice(special))

    remaining_length = length - len(required_charecters)
    password = required_charecters

    for idx in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    
password = password_generator()
print(password)