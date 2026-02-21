# Receives user input and returns how many words is inside of it
uInput = input("Give a sentence: ")
amount = uInput.split(" ")
print(f"Amount of words is {len(amount)}")
