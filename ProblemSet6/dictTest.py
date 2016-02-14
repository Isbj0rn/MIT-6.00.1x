cipher = {'a':'b', 'b':'c', 'c':'d', 'd':'e'}
text = 'abcd a'
newtext = []
for letter in text:
    if letter in cipher.keys():
        newtext.append(cipher[letter])
    else:
        newtext.append(letter)
encryptedText = ''.join(newtext)

print encryptedText
