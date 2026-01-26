def main():
    while True:
        userInput = input("Anna syöte (Lopeta lopettaa): ")
        if userInput == "Lopeta":
            break
        elif len(userInput) >=5:
            otherFunction(userInput)
        else:
            otherFunction()

def otherFunction(value = "Oletustulostus"):
    print(value)

if __name__ == "__main__":
    main()

