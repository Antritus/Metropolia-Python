def main():
    while True:
        userInput = input("Anna syöte (Lopeta lopettaa): ")
        if userInput == "Lopeta":
            break
        length = otherFunction(userInput)
        if length <= 0:
            print("Et antanut syötettä")
        else:
            print("Antamasi syöte oli", length, "merkkiä pitkä.")

def otherFunction(value):
    return len(value)

if __name__ == "__main__":
    main()

