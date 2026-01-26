userInput = input("Anna luku:")

try:
    number = int(userInput)
    print("Syöte oli kelvollinen.")
except (TypeError, ValueError):
    print("Virheellinen syöte!")