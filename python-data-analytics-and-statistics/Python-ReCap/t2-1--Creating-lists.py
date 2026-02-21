# Check what different list types do and which matches the matchable value
match = [2, 6, 12, 20, 30, 42]
values = {
    "a": [num*2 for num in range(6)],
    "b": [num**2 + 2 for num in range(1, 6)],
    "c": [num**2 + num for num in range(6)],
    "d": [num**2 + num for num in range(1, 7)]
}

for key in values:
    value = values[key]
    if (value == match):
        print("Match: "+ key)