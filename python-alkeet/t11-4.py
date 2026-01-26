import time

fileName = "muistio.txt"
try:
    with open(fileName) as file:
        file.close()
except IOError:
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")
    file = open(fileName, "w")
    file.close()

while (True):
    print("Käytetään muistiota:", fileName)
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Tyhjennä muistikirja")
    print("(4) Vaihda muistiota")
    print("(5) Lopeta")
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
        file.write(userInput + ":::" + time.strftime("%X %x"))
        file.close()
    elif (userInput == "3"):
        file = open(fileName, "w")
        file.close()
        print("Muistio tyhjennetty.")
    elif (userInput == "4"):
        fileName = input("Anna tiedoston nimi: ")
        try:
            with open(fileName) as file:

                file.close()
        except IOError:
            print("Tiedostoa ei löydy, luodaan tiedosto.")
            file = open(fileName, "w")
            file.close()
    elif (userInput == "5"):
        print("Lopetetaan.")
        break
