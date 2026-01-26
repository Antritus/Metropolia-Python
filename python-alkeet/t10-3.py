def testaa(password):
    if (len(password) < 5):
        return False

    digits = False;
    alphabet = False;
    for char in password[:]:
        if (char.isdigit() == True):
            digits = True
        elif (char.isalpha() == True):
            alphabet = True
    return digits and alphabet