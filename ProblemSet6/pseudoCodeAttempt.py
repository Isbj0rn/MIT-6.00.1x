def findBestShift(wordList, text):
    message = text.split(' ')
    shift = 0
    count = 0
    highestCount = 0
    mostWordsShift = None
    while shift < 26:
        attempt = applyShift(text, shift)
        message = attempt.split(' ')
        count = 0
        for word in message:
            if word in wordList:
                count += 1
        if count > highestCount:
            highestCount = count
            mostWordsShift = shift
        shift += 1
    return 'Shift required = ' + shift
    return 'Message: ' + attempt
