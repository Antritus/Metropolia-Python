firstValue = int(input("Anna ensimmäinen luku: "))
secondValue = int(input("Anna toinen luku: "))
print(" (1) +\n (2) -\n(3) *\n (4) /")
manipulator = int(input("Tee valinta (1-4): "))

if (manipulator == 1):
    value = firstValue + secondValue
    print("Tulos on: ", value)
elif (manipulator == 2):
    value = firstValue - secondValue
    print("Tulos on: ", value)
elif (manipulator == 3):
    value = firstValue * secondValue
    print("Tulos on: ", value)
elif (manipulator == 4):
    value = firstValue / secondValue
    print("Tulos on: ", value)
else:
    print("Valintaa ei tunnistettu.")