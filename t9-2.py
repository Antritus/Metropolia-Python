def main():
    inputValue = input("Anna lukuarvo: ")
    power = toinenpotenssi(int(inputValue))
    print("Toinen potenssi on", power)


def toinenpotenssi(value):
    return value**2

if __name__ == "__main__":
    main()