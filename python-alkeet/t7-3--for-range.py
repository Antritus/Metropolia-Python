userInput = int(input("Kuinka monta kierrosta?: "))
value = 0

for i in range(userInput):
    value = value + i

print("Kertymäksi saatiin: ", value)