''' creating a password generator that will pick characters from available characters(upper case, lower case, digits, special characters)
It should contain atleast one of each character type.
'''

import random
import string

def password_generator():             #defining a function called password_generator
    while True:
        try:                          # using exceptional handelling, so that user does not give wrong values
            length = int(input("Enter the password length: ").strip())

            if length < 5:               # codition used for getting password length greater than 5
                print("Password length must be at least 5 characters.")
                continue

            break

        except ValueError:
            print("Enter a valid number...")
  
    # Getting user's preferences   
    include_uppercase = input("Do you wanna include uppercase letters? (y/n): ").lower().strip()  
    include_lowercase = input("Do you wanna include lowercase letters? (y/n): ").lower().strip()
    include_digits = input("Do you wanna include digits? (y/n): ").lower().strip()
    include_special = input("Do you wanna include special characters? (y/n): ").lower().strip()

# Here python is using it's random module to give accurate passwors using user's preffered characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    all_characters = upper + lower + digits + special       # This is the variable that will be used at last as a final password

    required_charecters = []
    if include_uppercase == "y":
        required_charecters.append(random.choice(upper))
    if include_lowercase == "y":
        required_charecters.append(random.choice(lower))
    if include_digits == "y":
        required_charecters.append(random.choice(digits))
    if include_special == "y":
        required_charecters.append(random.choice(special))

    remaining_length = length - len(required_charecters)    # Let's assume the user choosed the password length 10, so in that case this variable will give the remaining length after appending all must-used characters
    password = required_charecters

    for idx in range(remaining_length):                   
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)                                # as the function is putting all the nessesary characters 1st and then adding random characters on it's choice, there should be no biased password, that's why it's using suffle

    str_password = "".join(password)                        # This is converting the list of characters to a string
    return str_password
password = password_generator()                             # calling the function.
print(password)