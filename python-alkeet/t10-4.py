import math

firstValue = int(input("Anna ensimmäinen luku: "))
secondValue = int(input("Anna toinen luku: "))
while(True):
    print(" (1) +\n (2) -\n (3) *\n (4) /\n (5) sin(luku1/luku2)\n (6) cos(luku1/luku2)\n (7)Vaihda luvut\n (8)Lopeta")
    print("Valitut luvut: ", firstValue, secondValue)
    manipulator = int(input("Tee valinta (1-8): "))

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
    elif (manipulator == 5):
        value = math.sin(firstValue/secondValue)
        print("Tulos on: ", value)
    elif (manipulator == 6):
        value = math.cos(firstValue / secondValue)
        print("Tulos on: ", value)
    elif (manipulator == 7):
        firstValue = int(input("Anna uusi ensimmäinen luku: "))
        secondValue = int(input("Anna uusi toinen luku: "))
    elif (manipulator == 8):
        break
    else:
        print("Valintaa ei tunnistettu.")