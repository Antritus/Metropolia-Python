firstValue = int(input("Anna ensimmäinen luku: "))
secondValue = int(input("Anna toinen luku: "))
while(True):
    print(" (1) +\n (2) -\n (3) *\n (4) /\n (5)Vaihda luvut\n (6)Lopeta")
    print("Valitut luvut: ", firstValue, secondValue)
    manipulator = int(input("Tee valinta (1-6): "))

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
        firstValue = int(input("Anna uusi ensimmäinen luku: "))
        secondValue = int(input("Anna uusi toinen luku: "))
    elif (manipulator == 6):
        break
    else:
        print("Valintaa ei tunnistettu.")