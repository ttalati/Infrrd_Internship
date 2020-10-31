import json
import os.path

keyWord = input("What is the word? ")
count = 100
globalWords = []
save_path = "C:/Users/Tejas/PycharmProjects/Tokenizer/data"

while(count > 0):
    words = []
    keyString = ""
    name_file = "testfile" + str(count) + ".txt"

    name = os.path.join("C:/Users/Tejas/PycharmProjects/Tokenizer/data", name_file)

    with open(name, 'r') as f:
        for line in f:
            keyString = keyString + line

    keyString = keyString.replace("'", " ")
    keyString = keyString.replace(".", " ")
    keyString = keyString.replace("\"", " ")
    keyString = keyString.replace(",", " ")
    keyString = keyString.replace(":", " ")
    keyString = keyString.replace("(", " ")
    keyString = keyString.replace(")", " ")
    keyString = keyString.replace("_", " ")

    arrayString = keyString.split()
    indexcount = 0
    indexes = []
    wordCount = 0

    for string in arrayString:
        if string == keyWord:
            indexes.append(indexcount)
            wordCount = wordCount + 1
        indexcount = indexcount + 1

    if wordCount > 0:
        globalWords.append({'fileName': name_file, 'token': keyWord, 'wordCount': wordCount, 'indexes': indexes})
    count = count - 1

print(sorted(globalWords, key=lambda i: i['wordCount'], reverse=True))
newList = sorted(globalWords, key=lambda i: i['wordCount'], reverse=True)
print("Number of matches " + str(len(newList)))
if len(newList) > 0:
    print("Largest number: " + str(newList[0].get('wordCount')))
print("\n")

with open('scratch.json5', 'w') as file:
    json.dump(globalWords, file)
