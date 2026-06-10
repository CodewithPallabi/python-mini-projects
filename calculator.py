#Calculator made by simple if-else conditions:
while True:                                                 # creating an infinite loop for exceptional handeling until user give two valid numbers.
    try:
        num1 = int(input("Enter 1st number: "))             # taking input from user as number
        num2 = int(input("Enter 2nd number: "))
        break                                               # if user give two valid numbers this loop will break and the code will move forward
    except ValueError:
        print("Please enter valid numbers..")

opr = input("Enter your operator: ")                # taking input from user as arithmetic operators
if num1>=num2:                                      # checking which number is bigger using conditions
    if opr=="+":
        print(num1+num2)
    if opr=="-":
        print(num1-num2)
    if opr=="/":
        print(num1/num2)
    if opr=="*":
        print(num1*num2)

elif num2>=num1:
    if opr=="+":
        print(num1+num2)
    if opr=="-":
        print(num2-num1)
    if opr=="/":
        print(num2/num1)
    if opr=="*":
        print(num1*num2)
else:                                             
    print("it's an error")
    