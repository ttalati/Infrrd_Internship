import os
import json

count = 100
main_dictionary = {}

while count > 0:
    keyString = ""
    name_file = "testfile" + str(count) + ".txt"
    name = os.path.join("C:/Users/Tejas/PycharmProjects/Tokenizer/data", name_file)

    with open(name, 'r') as f:
        for line in f:
            keyString = keyString + line

    keyString = keyString.replace("'", " ")
    keyString = keyString.replace(".", " ")
    keyString = keyString.replace("\"", " ") #words --> file ---> index , thisWordCount, total word_count
    keyString = keyString.replace(",", " ")
    keyString = keyString.replace(":", " ")
    keyString = keyString.replace("(", " ")
    keyString = keyString.replace(")", " ")
    keyString = keyString.replace("_", " ")

    array_string = keyString.split()
    index_count = 0

    for string in array_string:
        stringLow = string.lower()
        if stringLow[0:1] in main_dictionary.keys():
            if stringLow in main_dictionary[stringLow[0:1]].keys():
                if name_file in main_dictionary[stringLow[0:1]][stringLow].keys():
                    main_dictionary[stringLow[0:1]][stringLow][name_file][0].append(index_count)
                    main_dictionary[stringLow[0:1]][stringLow][name_file][1] = main_dictionary[stringLow[0:1]][stringLow][name_file][1] + 1
                else:
                    main_dictionary[stringLow[0:1]][stringLow][name_file] = [[index_count], 1, len(array_string)]
            else:
                main_dictionary[stringLow[0:1]][stringLow] = {}
                main_dictionary[stringLow[0:1]][stringLow][name_file] = [[index_count], 1, len(array_string)]
        else:
            main_dictionary[stringLow[0:1]] = {}
            main_dictionary[stringLow[0:1]][stringLow] = {}
            main_dictionary[stringLow[0:1]][stringLow][name_file] = [[index_count], 1, len(array_string)]
        index_count = index_count + 1
    count = count - 1

for key in main_dictionary.keys():
    name_file = "datafile" + key + ".json5"
    name = os.path.join("C:/Users/Tejas/PycharmProjects/Tokenizer/data", name_file)
    with open(name, 'w') as file:
        json.dump(main_dictionary[key], file)

