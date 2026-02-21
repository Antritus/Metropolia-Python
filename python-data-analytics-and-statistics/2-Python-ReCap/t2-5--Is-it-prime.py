uInput = input("Give a number: ")

try:
    intInput = int(uInput)

    if intInput <= 1:
        print(f"{intInput} is not a prime number")
    else:
        is_prime = True

        for num in range(2, intInput):
            if intInput % num == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{intInput} is a prime number")
        else:
            print(f"{intInput} is not a prime number")

except ValueError:
    print(f"{uInput} is not a valid number")