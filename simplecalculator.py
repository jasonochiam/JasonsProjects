def calculate():
    operation = input('''Welcome to Jasons Calculator! Please press the following:
+ for addition
- for subtraction
/ for division
* for multiplication
''')
    num1 = int(input('Type your first number: '))
    num2 = int(input('Type your second number: '))

    if operation == "+":
        print(str(num1) + " + " + str(num2) + " =")
        print(num1 + num2)

    elif operation == "-":
        print(str(num1) + " - " + str(num2) + " =")
        print(num1 - num2)

    elif operation == "/":
        print(str(num1) + " / " + str(num2) + " =")
        print(num1 / num2)

    elif operation == "*":
        print(str(num1) + " * " + str(num2) + " =")
        print(num1 * num2)

    else:
        print("Please use a valid operation!")
    
    again()


def again():
    choice = input('''Do you want to calculate again?
    Type Y for yes or N for no!''')

    if choice == "Y":
        calculate()

    elif choice == "N":
        print("Thank you for using my calculator!")

    else:
        print("That was not a valid input. Please try again!")
        again()

calculate()


