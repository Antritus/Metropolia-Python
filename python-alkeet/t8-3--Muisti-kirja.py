fileName = "muistio.txt"
while (True):
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Tyhjennä muistikirja")
    print("(4) Lopeta")
    print("")
    userInput = input("Mitä haluat tehdä?: ")

    if (userInput == "1"):
        file = open(fileName, "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()
    elif (userInput == "2"):
        file = open(fileName, "a")
        userInput = input("Kirjoita uusi merkintä: ")
        file.write(userInput)
        file.close()
    elif (userInput == "3"):
        file = open(fileName, "w")
        file.close()
        print("Muistio tyhjennetty.")
    elif (userInput == "4"):
        print("Lopetetaan.")
        break