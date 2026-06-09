Name = input("Enter your name: ")
print(f"Hello {Name}!\nEnter your birth details bellow....")

birth_date = int(input("Enter your birth date: "))
if birth_date < 1 or birth_date > 31:
    print("Invalid birth date!")
    exit()
birth_month = int(input("Enter your birth month: "))
if birth_month < 1 or birth_month > 12:
    print("Invalid birth month!")
    exit()
birth_year = int(input("Enter your birth year: "))

current_date = int(input("Enter today's date: "))
if current_date < 1 or current_date > 31:
    print("Invalid date!")
    exit()
current_month = int(input("Enter current month: "))
if current_month < 1 or current_month > 12:
    print("Invalid month!")
    exit()
current_year = int(input("Enter current year: "))

if (birth_year, birth_month, birth_date) > (current_year, current_month, current_date):
    print("Birth date cannot be in the future!")
    exit()

date = current_date - birth_date
month = current_month - birth_month
year = current_year - birth_year

if date < 0:
    date += 31      # temporary taking the day value of the previous month = 31 days(june for me)
    month -= 1

if month < 0:
    month += 12
    year -= 1

print(f"your are {year}years, {month}months, {date}days old.")