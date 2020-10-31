import json
import os
import math
import nltk

findWord = input("What word do you want to find? ")
text_file = "datafile" + findWord[0:1] + ".json5"
name = os.path.join("C:/Users/Tejas/PycharmProjects/Tokenizer/data", text_file)

with open(name, 'r') as json_file:
    data = json.load(json_file)

    score_list = []
    numCount = 0 #tfidf, stemming, lemmatization
    for key in data.keys():
        if key == findWord:
            for fileName in data[findWord].keys():
                score = data[findWord][fileName][1]/data[findWord][fileName][2]
                score = score * math.log10(100/len(data[findWord]))
                score_list.append({"file": fileName, "score": score})

    score_list = sorted(score_list, key=lambda i: i["score"], reverse=True)
    print("Best score file name: " + score_list[0]["file"] + " score: " + str(score_list[0]["score"]))
