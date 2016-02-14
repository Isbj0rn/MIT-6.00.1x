import string


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList


def applyShift(text, shift):
    return applyCoder(text, buildCoder(shift))

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
        
    return cipher

def applyCoder(text, cipher):
    newtext = []
    for letter in text:
        if letter in cipher.keys():
            newtext.append(cipher[letter])
        else:
            newtext.append(letter)
    encryptedText = ''.join(newtext)

    return encryptedText


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    shift = 0
    count = 0
    highestCount = 0
    mostWordsShift = None
    while shift < 26:
        attempt = applyShift(text, shift)
        message = attempt.split(' ')
        count = 0
        if isWord(wordList, word) == True:
                count += 1
        if count > highestCount:
            highestCount = count
            mostWordsShift = shift
        shift += 1
    return 'Shift required = ' + shift
    return 'Message: ' + attempt
