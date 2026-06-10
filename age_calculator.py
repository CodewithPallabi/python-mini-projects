Name = input("Enter your name: ")
print(f"Hello {Name}!\nEnter your birth details bellow....")
# Get and validate user's birth date
while True:
    try:                                                      # handelling error.
        birth_date = int(input("Enter your birth date: "))
        if birth_date < 1 or birth_date > 31:
            print("Invalid birth date!")
            exit()
        break
    except ValueError:
        print("Please enter a numeric value...")
# Get and validate user's birth month
while True:
    try:                                                      # handelling error.
        birth_month = int(input("Enter your birth month: "))
        if birth_month < 1 or birth_month > 12:
            print("Invalid birth month!")
            exit()
        break    
    except ValueError:
        print("Please enter a numeric value...")
# Get and validate user's birth year
while True:
    try:                                                     # handelling error.
        birth_year = int(input("Enter your birth year: "))
        break
    except ValueError:
        print("Please enter a numeric value...")

# Get and validate current date
while True:
    try:
        current_date = int(input("Enter today's date: "))
        if current_date < 1 or current_date > 31:
            print("Invalid date!")
            exit()
        break   
    except ValueError:
        print("Please enter a numeric value...")

# Get and validate current month
while True:
    try:
        current_month = int(input("Enter current month: "))
        if current_month < 1 or current_month > 12:
            print("Invalid month!")
            exit()
        break
    except ValueError:
        print("Please enter a numeric value...")     

# Get and validate current year
while True:
    try:
        current_year = int(input("Enter current year: "))
        break
    except ValueError:
        print("Please enter a numeric value...")
# Checking if the birth date is in the future
if (birth_year, birth_month, birth_date) > (current_year, current_month, current_date):
    print("Birth date cannot be in the future!")
    exit()

date = current_date - birth_date
month = current_month - birth_month
year = current_year - birth_year

if date < 0:                                                  # Borrow days from the previous month if needed
    if current_month == 3:                                                                        # This block is for february month
        if (current_year % 400 == 0) or (current_year % 4 == 0 and current_year % 100 != 0):      # Checking for leap year
            date += 29
        else:
            date += 28
    elif current_month in [5, 7, 10, 12]:
        date += 30
    else:
        date += 31

    month -= 1
if month < 0:                                                 # Borrow months from the previous year if needed
    month += 12
    year -= 1

print(f"your are {year}years, {month}months, {date}days old.")