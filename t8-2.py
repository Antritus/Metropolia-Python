file = open("merkkijonoja.txt", "r")
lines = file.readlines()

for line in lines:
    line = line.replace("\n", "")
    if line.isalnum():
        print(line, "kelpaa salasanaksi.")
    else:
        print(line, "sisältää virheellisiä merkkejä.")
