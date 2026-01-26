firstValue = int(input("Anna luku: "))
secondValue = int(input("Anna toinen luku: "))

if (firstValue % 2 == 0 and secondValue % 2 == 0):
    print("Molemmat luvut ovat parillisia.")
elif (firstValue % 2 == 0 or secondValue % 2 == 0):
    print("Toinen luku on parillinen.")
else:
    print("Molemmat luvut ovat parittomia.")
