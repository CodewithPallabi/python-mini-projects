#Calculator made by simple if-else conditions:
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
opr = input("Enter your operator: ")
if num1>=num2:
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
    