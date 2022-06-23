wordList = [str(word) for word in input("Enter word list: ").split(', ')]
wordSet = set(wordList)
wordSetLength = len(wordSet)
print("This word set cotains {0} word(s).".format(wordSetLength))

print("Enter second list with {0} elements: ".format(wordSetLength))
valueList = list()
for i in range(0, wordSetLength, 1):
    valueList.append(input("Enter {0}-th value: ".format(i)))

dictionary = {}
for word, value in zip(wordSet, valueList):
    dictionary.setdefault(word, value)

print("Created dictionary: {0}".format(dictionary))