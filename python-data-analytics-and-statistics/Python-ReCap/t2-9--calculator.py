import math

number1 = "a"
while number1 == "a":
    try:
        number1 = int(input("Give the first number: "))
    except ValueError:
        print("Invalid input!")

number2 = "a"
while number2 == "a":
    try:
        number2 = int(input("Give the second number: "))
    except ValueError:
        print("Invalid input!")

while(True):
    print(" (1) +\n (2) -\n (3) *\n (4) /\n (5)Change numbers\n (6)Quit")
    print("Current numbers: ", number1, number2)
    selection = int(input("Please select something (1-6): "))

    if (selection == 1):
        value = number1 + number2
        print("The result is: ", value)
    elif (selection == 2):
        value = number1 - number2
        print("The result is: ", value)
    elif (selection == 3):
        value = number1 * number2
        print("The result is: ", value)
    elif (selection == 4):
        value = number1 / number2
        print("The result is: ", value)
    elif (selection == 5):
        number1 = "a"
        while number1 == "a":
            try:
                number1 = int(input("Give the first number: "))
            except ValueError:
                print("Invalid input!")

        number2 = "a"
        while number2 == "a":
            try:
                number2 = int(input("Give the second number: "))
            except ValueError:
                print("Invalid input!")
    elif (selection == 6):
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")