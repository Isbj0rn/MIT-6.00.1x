import string

def removePunctuation(text):
    for item in text:
        for item in string.punctuation:
            string.replace(text, item, ' ')
    return text
