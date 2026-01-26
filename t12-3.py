file = open("sanoja.txt", "r")
values = file.readlines()
values.sort()

print("Sanat laitettuna aakkosjärjestykseen:")
for value in values:
    print(value)
    