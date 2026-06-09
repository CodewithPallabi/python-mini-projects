import random

number_to_guess = random.randint(0, 100)
while True:
    try:
        guess = int(input("Geuss the number between 1 to 100: "))

        if guess > number_to_guess :
            print("Too high!!")
        elif guess < number_to_guess :
            print("Too low!!")
        else:
            print("congragulations!!This is the right number.")
            break

    except ValueError :
        print("Enter a valid number...")


