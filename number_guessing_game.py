import random                                        #importing random module for generating random numbers.

number_to_guess = random.randint(0, 100)             # generates a random number between 0 and 100.
while True:                                          # creates an infinite loop that runs until the user guesses the correct number.
    try:                                             # handelling error(if user answer with any alphabet or special character it'll handle the error)
        guess = int(input("Geuss the number between 1 to 100: ")) #taking input from user.

        if guess > number_to_guess :                 # giving conditions
            print("Too high!!")
        elif guess < number_to_guess :
            print("Too low!!")
        else:
            print("congragulations!!This is the right number.")  
            break                                    # if the answer is correct the loop will break with a congragulations statement.

    except ValueError :
        print("Enter a valid number...")


