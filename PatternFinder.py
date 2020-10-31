# --------------------------Start--------------------------------------------------------------------------------------#
# ----------------------------Input Frequencies------------------------------------------------------------------------#

import time

start_time = time.time()
file = open("output.txt", "r+")

letter_list = [{}]

for id_text in file:
    # print(id_text[0:1])
    for i in range(len(id_text) - 1):
        # print(i)
        if len(letter_list) < i + 1:
            letter_list.append({})
        # print(letter_list)
        if id_text[i:i + 1] in letter_list[i].keys():
            letter_list[i][id_text[i:i + 1]] = letter_list[i][id_text[i:i + 1]] + 1
        else:
            letter_list[i].update({id_text[i:i + 1]: 1})

print("Input Frequencies:")
print(letter_list)

# -----------------------------------------------Output Frequencies----------------------------------------------------#

file = open("input.txt", "r+")

letter_two_list = [{}]

for id_text in file:
    # print(id_text[0:1])
    for i in range(len(id_text) - 1):
        # print(i)
        if len(letter_two_list) < i + 1:
            letter_two_list.append({})
        # print(letter_list)
        if id_text[i:i + 1] in letter_two_list[i].keys():
            letter_two_list[i][id_text[i:i + 1]] = letter_two_list[i][id_text[i:i + 1]] + 1
        else:
            letter_two_list[i].update({id_text[i:i + 1]: 1})

print("\n" + "Output Frequencies:")
print(letter_two_list)

# ----------------------------Difference Frequencies-------------------------------------------------------------------#

difference_freq = []

for number in range(len(letter_two_list) - 1):
    difference_freq.append({})
    for i in letter_two_list[number].keys():
        if (number < len(letter_list)) and (i in letter_list[number].keys()):
            difference_freq[number].update({i: letter_two_list[number][i] - letter_list[number][i]})
        else:
            difference_freq[number].update({i: letter_two_list[number][i]})

print("\n" + "Difference Frequencies:")
print(difference_freq)

# -------------------------------Two Grams Input-----------------------------------------------------------------------#

file = open("output.txt", "r+")
two_gram_input = []
i = 0
for word in file:
    two_gram_input.append([])
    for x in range(len(word)):
        n = word[x:x + 2]
        two_gram_input[i].append(n)
    i = i + 1

print("\n" + "Two Gram Input")
print(two_gram_input)

# -----------------------------Two Gram Outputs------------------------------------------------------------------------#

file = open("input.txt", "r+")
two_gram_output = []
i = 0
for word in file:
    two_gram_output.append([])
    for x in range(len(word)):
        n = word[x:x + 2]
        two_gram_output[i].append(n)
    i = i + 1

print("\n" + "Two Gram Output")
print(two_gram_output)

# ---------------------------Frequency Grams Input---------------------------------------------------------------------#

freq_gram = [{}]

for i in range(len(two_gram_input)):
    for gram in two_gram_input[i]:
        if gram in freq_gram[0].keys():
            freq_gram[0][gram] = freq_gram[0][gram] + 1
        else:
            freq_gram[0].update({gram: 1})

print()
print("Frequency 2-gram Input:")
print(freq_gram)

# --------------------------Frequency Grams Output---------------------------------------------------------------------#

freq_gram_output = [{}]

for i in range(len(two_gram_output)):
    for gram in two_gram_output[i]:
        if gram in freq_gram_output[0].keys():
            freq_gram_output[0][gram] = freq_gram_output[0][gram] + 1
        else:
            freq_gram_output[0].update({gram: 1})

print()
print("Frequency 2-gram Output:")
print(freq_gram_output)

# ---------------------------Difference Frequency Gram-----------------------------------------------------------------#

difference_freq_gram = {}

for key in freq_gram_output[0].keys():
    if key in freq_gram[0].keys():
        # difference_freq_gram.update({key: freq_gram_output[key] - freq_gram[0][key]})
        difference_freq_gram.update({key: freq_gram_output[0][key] - freq_gram[0][key]})
    else:
        difference_freq_gram.update({key: freq_gram_output[0][key]})

for key in freq_gram[0].keys():
    if not (key in freq_gram_output[0].keys()):
        # difference_freq_gram.update({key:freq_gram[0][key]})
        difference_freq_gram.update({key: -1 * freq_gram[0][key]})

print()
print("Frequency Difference in 2-Gram")
print(difference_freq_gram)

# --------------------------------Sorted Ascending---------------------------------------------------------------------#

sorted_d = sorted(difference_freq_gram.items(), key=lambda x: x[1])

print()
print('Difference frequency in ascending order by value:')
print(sorted_d)

# --------------------------------Sorted Descending--------------------------------------------------------------------#

sorted_freq = dict(sorted(difference_freq_gram.items(), key=lambda x: x[1], reverse=True))

print()
print('Difference Frequency in descending order by value: ')
print(sorted_freq)

# --------------------------------------Mapping Input and Output 2 Grams-----------------------------------------------#

mapping = {}

for i in range(len(two_gram_input)):
    for j in range(len(two_gram_input[i])):
        if j < len(two_gram_output[i]):
            if two_gram_input[i][j] in mapping.keys():
                temp = two_gram_input[i][j]
                if two_gram_output[i][j] in mapping[temp].keys():
                    temp_two = two_gram_output[i][j]
                    mapping[temp][temp_two] = mapping[temp][temp_two] + 1
                else:
                    temp_two = two_gram_output[i][j]
                    mapping[temp].update({temp_two: 1})
            else:
                temp = two_gram_input[i][j]
                mapping.update({temp: {two_gram_output[i][j]: 1}})

print()
print("Mapping of Specific Input Grams to Corresponding Output Grams:")
print(mapping)

# ------------------------------Input One Gram-------------------------------------------------------------------------#

file = open("output.txt", "r+")
one_gram_input = []

i = 0
for word in file:
    one_gram_input.append([])
    for x in range(len(word)):
        n = word[x:x + 1]
        one_gram_input[i].append(n)
    i = i + 1

print()
print("One Gram Input:")
print(one_gram_input)

# --------------------------------------Output One Gram----------------------------------------------------------------#

file = open("input.txt", "r+")
one_gram_output = []

i = 0
for word in file:
    one_gram_output.append([])
    for x in range(len(word)):
        n = word[x:x + 1]
        one_gram_output[i].append(n)
    i = i + 1

print("\n" + "One Gram Output")
print(one_gram_output)

# --------------------------Double Two Gram Input----------------------------------------------------------------------#

file = open("output.txt", "r+")
double_two_gram_input = []

i = 0
for word in file:
    double_two_gram_input.append([])
    for x in range(len(word)):
        n = word[x:x + 2]
        double_two_gram_input[i].append(n)
        double_two_gram_input[i].append(n)
    i = i + 1

print()
print("Duplicate Two Gram Input:")
print(double_two_gram_input)

# -------------------------Mapping Two to One--------------------------------------------------------------------------#

import math
two_one_mapping = {}

for i in range(len(double_two_gram_input)):
    for j in range(len(double_two_gram_input[i])):
        if math.trunc(j/2) < len(one_gram_output[i]):
            if double_two_gram_input[i][j] in two_one_mapping.keys():
                temp = double_two_gram_input[i][j]
                if one_gram_output[i][math.trunc(j/2)] in two_one_mapping[temp].keys():
                    temp_two = one_gram_output[i][math.trunc(j/2)]
                    two_one_mapping[temp][temp_two] = two_one_mapping[temp][temp_two] + 1
                else:
                    temp_two = one_gram_output[i][math.trunc(j/2)]
                    two_one_mapping[temp].update({temp_two: 1})
            else:
                temp = double_two_gram_input[i][j]
                two_one_mapping.update({temp: {one_gram_output[i][math.trunc(j/2)]: 1}})

print()
print("Mapping of Specific Input Grams to Corresponding Output Grams (Two to One):")
print(two_one_mapping)

# ------------------------------Pattern Finding------------------------------------------------------------------------#

file = open("output.txt", "r+")
words = []

for i in file:
    words.append(i)

pattern_mapping = []

for word in words:
    for i in range(len(word) - 1):
        if len(pattern_mapping) <= i:
            pattern_mapping.append({})
            # print(pattern_mapping)
        if word[0:i+1] in pattern_mapping[i].keys():
            pattern_mapping[i][word[0:i+1]].append(word[i:len(word)])
        else:
            pattern_mapping[i].update({word[0:i+1]: [word[i:len(word)]]})

print()
print("Pattern Finding: ")
print(pattern_mapping)

# ------------------------------------- Error Map Formation------------------------------------------------------------#

# here would be an error map

# -------------------------Pattern Finding Json Export-----------------------------------------------------------------#

import json

with open('pattern.json5', 'w') as outfile:
    json.dump(pattern_mapping, outfile)

# ---------------------------Mapping Json Export-----------------------------------------------------------------------#

with open('data.json5', 'w') as outfile:
    json.dump(mapping, outfile)

# --------------------------Two To One Mapping Json Export-------------------------------------------------------------#

with open('two_one_data.json5', 'w') as outfile:
    json.dump(two_one_mapping, outfile)

# --------------------------Timing Print-------------------------------------------------------------------------------#

print()
print("--- %s seconds ---" % (time.time() - start_time))

# -------------------------Ending--------------------------------------------------------------------------------------#
