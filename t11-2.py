try:
    fileName = input("Anna tiedoston nimi: ")
    file = open(fileName, "r")
    value = file.readline()
    valueInt = int(value) + 313
    print("Saatiin tulos", valueInt)
except (TypeError, ValueError):
    print("Tiedoston sisältö virheellinen!")
except IOError:
    print("Virheellinen tiedostonnimi")