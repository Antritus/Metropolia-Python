realPassword = "Esimerkki"
realName = "Erkki"

inputName = input("Anna nimi: ")
if (inputName == realName):
    inputPassword = input("Anna salasana: ")
    if (realPassword == inputPassword):
        print("Salasana ja nimi oli oikein!")
    else:
        print("Salasana oli väärin.")
else:
    print("Nimi oli väärin.")