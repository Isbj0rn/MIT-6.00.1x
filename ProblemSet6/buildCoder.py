import string

def buildCoder(shift):
    cipher = {}
    alphabet = []
    move = -51 + (shift -1)
    for letter in string.ascii_lowercase:
        alphabet.append(letter)
    for Uletter in string.ascii_uppercase:
        alphabet.append(Uletter)
    for i in alphabet:
        if i.isupper():
            cipher[i] = alphabet[alphabet.index(i) + move].upper()
        elif i.islower():
            cipher[i] = alphabet[alphabet.index(i) + move].lower()
        
    print cipher
