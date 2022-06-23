def getWordList():
    return [str(word) for word in input("Enter word list: ").split(', ')]

def wordListToSet(wordList):
    wordSet = set(wordList)
    wordSetLength = len(wordSet)
    print("This word set cotains {0} word(s).".format(wordSetLength))
    return wordSet

def getValueList(length):
    print("Enter value list with {0} elements: ".format(length))
    valueList = list()
    for i in range(0, length, 1):
        valueList.append(input("Enter {0}-th value: ".format(i)))
    return valueList

def createDictionary(words, values):
    dictionary = {}
    for word, value in zip(words, values):
        dictionary.setdefault(word, value)
    return dictionary

def main():
    wordList = getWordList()
    wordSet = wordListToSet(wordList)
    valueList = getValueList(len(wordSet))
    createdDictionary = createDictionary(wordSet, valueList)
    print("Created dictionary: {0}".format(createdDictionary))

main()