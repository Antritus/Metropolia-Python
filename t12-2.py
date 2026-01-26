values = []

while True:
    print("Haluatko")
    print("(1)Lisätä listaan")
    print("(2)Poistaa listalta vai")
    userInput = input("(3)Lopettaa?: ")
    if userInput == "1":
        userInput = input("Mitä lisätään?: ")
        values.append(userInput)
    elif userInput == "2":
        userInput = input(f"Listalla on {values.__len__()} alkiota.\nMonesko niistä poistetaan?: ")
        if (int(userInput) > values.__len__()):
            print("Virheellinen valinta.")
        else:
            values.pop(int(userInput))
    elif userInput == "3":
        print("Listalla oli tuotteet:")
        for val in values:
            print(f"{val}")
        break
    else:
        print("Virheellinen valinta.")