import time

fileData = []
fileName = "muistio.dat"
try:
    with open(fileName) as file:
        fileData = file.readlines()
        file.close()
except IOError:
    print(f"Virhe tiedostossa, luodaan uusi {fileName}.")
    file = open(fileName, "w")
    fileData = []
    file.close()

while (True):
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Muokkaa merkintää")
    print("(4) Poista merkintä")
    print("(5) Tallenna ja lopeta")
    print("")
    currentNode = 0
    userInput = input("Mitä haluat tehdä?: ")

    if (userInput == "1"):
        for line in fileData:
            print(line)
    elif (userInput == "2"):
        file = open(fileName, "a")
        userInput = input("Kirjoita uusi merkintä: ")
        fileData.append(userInput + ":::" + time.strftime("%X %x"))
    elif (userInput == "3"):
        if len(fileData) == 0:
            print("Ei merkintöjä.")
            continue

        userInput = int(input(f"Listalla on {len(fileData)} merkintää.\nMitä niistä muutetaan?: "))

        if userInput < 1 or userInput > len(fileData):
            print("Virheellinen valinta.")
            continue

        currentNode = userInput - 1
        print(fileData[currentNode])
        userInputNew = input("Anna uusi teksti: ")
        fileData[currentNode] = userInputNew + ":::" + time.strftime("%X %x")
    elif (userInput == "4"):
        userInput = int(input(f"Listalla on {len(fileData)} merkintää.\nMitä niistä poistetaan?: "))
        currentNode = userInput - 1
        value = fileData.pop(currentNode)
        print("Poistettiin merkintä", value)
    elif (userInput == "5"):
        file = open(fileName, "w")
        for line in fileData:
            file.write(line + "\n")
        file.close()
        print("Lopetetaan.")
        break
