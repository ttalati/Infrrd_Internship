import json

words = []
keyString = ""
globalWords = []
name = "textBank.txt"

with open('textBank.txt', 'r') as f:
    for line in f:
        keyString = keyString + line

keyWord = input("What is the word? ")
keyString = keyString.replace("'", " ")
keyString = keyString.replace(".", " ")
keyString = keyString.replace("\"", " ")
keyString = keyString.replace(",", " ")
keyString = keyString.replace(":", " ")
keyString = keyString.replace("(", " ")
keyString = keyString.replace(")", " ")
keyString = keyString.replace("_", " ")

arrayString = keyString.split()
count = 0
indexes = []
wordCount = 0

for string in arrayString:
    if string == keyWord:
        indexes.append(count)
        # print("found " + keyWord +  " at index: " + str(count))
        wordCount = wordCount + 1
    count = count + 1

# print("Total Count: " + str(wordCount))
if wordCount > 0:
    globalWords.append({'fileName' : name ,'token': keyWord, 'wordCount': wordCount, 'indexes': indexes})

print("\n")

words = []
keyString = ""
with open('textBank.txt', 'r') as f:
    for line in f:
        keyString = keyString + line

keyWord = input("What is the word? ")
keyString = keyString.replace("'", " ")
keyString = keyString.replace(".", " ")
keyString = keyString.replace("\"", " ")
keyString = keyString.replace(",", " ")
keyString = keyString.replace(":", " ")
keyString = keyString.replace("(", " ")
keyString = keyString.replace(")", " ")
keyString = keyString.replace("_", " ")

arrayString = keyString.split()
count = 0
indexes = []
wordCount = 0

for string in arrayString:
    if string == keyWord:
        indexes.append(count)
        # print("found " + keyWord + " at index: " + str(count))
        wordCount = wordCount + 1
    count = count + 1

# print("Total Count: " + str(wordCount))

if wordCount > 0:
    globalWords.append({'fileName' : name ,'token': keyWord, 'wordCount': wordCount, 'indexes': indexes})

print("\n")

words = []
keyString = ""
with open('textBank.txt', 'r') as f:
    for line in f:
        keyString = keyString + line

keyWord = input("What is the word? ")
keyString = keyString.replace("'", " ")
keyString = keyString.replace(".", " ")
keyString = keyString.replace("\"", " ")
keyString = keyString.replace(",", " ")
keyString = keyString.replace(":", " ")
keyString = keyString.replace("(", " ")
keyString = keyString.replace(")", " ")
keyString = keyString.replace("_", " ")

arrayString = keyString.split()
count = 0
indexes = []
wordCount = 0

for string in arrayString:
    if string == keyWord:
        indexes.append(count)
        # print("found " + keyWord + " at index: " + str(count))
        wordCount = wordCount + 1
    count = count + 1

# print("Total Count: " + str(wordCount))

if wordCount > 0:
    globalWords.append({'fileName' : name ,'token': keyWord, 'wordCount': wordCount, 'indexes': indexes})

print("\n")

words = []
keyString = ""
with open('textBank.txt', 'r') as f:
    for line in f:
        keyString = keyString + line

keyWord = input("What is the word? ")
keyString = keyString.replace("'", " ")
keyString = keyString.replace(".", " ")
keyString = keyString.replace("\"", " ")
keyString = keyString.replace(",", " ")
keyString = keyString.replace(":", " ")
keyString = keyString.replace("(", " ")
keyString = keyString.replace(")", " ")
keyString = keyString.replace("_", " ")

arrayString = keyString.split()
count = 0
indexes = []
wordCount = 0

for string in arrayString:
    if string == keyWord:
        indexes.append(count)
        print("found " + keyWord + " at index: " + str(count))
        wordCount = wordCount + 1
    count = count + 1

# print("Total Count: " + str(wordCount))
if wordCount > 0:
    globalWords.append({'fileName' : name,'token': keyWord, 'wordCount': wordCount, 'indexes': indexes})


print(sorted(globalWords, key=lambda i: i['wordCount'], reverse=True))
newList = sorted(globalWords, key=lambda i: i['wordCount'], reverse=True)
print("Largest number: " + str(newList[0].get('wordCount')))
print("\n")

with open('scratch.json5', 'w') as file:
    json.dump(globalWords, file)