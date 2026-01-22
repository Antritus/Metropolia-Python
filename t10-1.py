import random

print("Heitetään kolikkoa viidesti:")
for i in range(5):
    value = random.randint(0, 1)
    if (value == 0):
        print("Klaava!")
    else:
        print("Kruuna!")