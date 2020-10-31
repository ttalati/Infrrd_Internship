import json
import os
import re
import nltk
import math
from nltk.stem import PorterStemmer 

files_paths = []

directory = r"C:\\Users\\Tejas\\Documents\\RandomText"
for entry in os.scandir(directory):
    if entry.path.endswith(".txt") and entry.is_file():
        files_paths.append(entry.path)
print("\n\n\n")

###------------------------GET ALL THE DATA INTO PROGRAM-----------------------------###

all_text = {}
file_names = "file_num:"
count  = 1

for entry in files_paths:
    with open(entry, 'r') as f:
        text = f.read()
        all_text[file_names + str(count)] = text
        count = count + 1

print("GATHERING DATA \n") 
print(all_text)
print("\n\n\n")

###-------------------------USING REGEX TO TOKENIZE-----------------------------------###

tokenized= {}

for entry in all_text:
    tokens = re.findall("[\w']+", all_text[entry])
    ###print(tokens)
    tokenized[entry] = tokens

print("TOKENIZING \n")   
print(tokenized)
print("\n\n\n")

###--------------------------STEMMING AND LEMMATAZATION------------------------------###

def stemming_wanted(wanted):
    if wanted:
        ps = PorterStemmer() 
        for entry in tokenized:
            for i in range(0, len(tokenized[entry])):
                tokenized[entry][i] = ps.stem(tokenized[entry][i])

stemming_wanted(True)

print("STEMMING \n")       
print(tokenized)
print("\n\n\n")

###--------------------------BAG OF WORDS---------------------------------------------###

bag_words = {}

for entry in tokenized:
    bag_words[entry] = {}
    for word in tokenized[entry]:
        if not word in bag_words[entry].keys():
            bag_words[entry][word] = 1
        else:
            bag_words[entry][word] = bag_words[entry][word] + 1

print("BAG OF WORDS/FREQUENCY LIST \n") 
print(bag_words)
print("\n\n\n")

###------------------------Ngram-----------------------------------------------------###

def make_ngram(n, tokens):
    repeat = n
    ngram_list = []
    count = 0
    for j in range(0, len(tokens)):
        if j + n <= len(tokens):
            local_string = ""
            for i in range(j, j + n, 1):
                local_string = local_string + tokens[i]
                if i < j + n:
                    local_string = local_string + " "
            ngram_list.append(local_string)
    ##print(ngram_list)
    return ngram_list

n_gram = {}
for entry in tokenized:
    n_gram[entry] = {}
    ngram_list = make_ngram(2, tokenized[entry])
    
    for word in ngram_list:
        if not word in n_gram[entry].keys():
            n_gram[entry][word] = 1
        else:
            n_gram[entry][word] = n_gram[entry][word] + 1

print("NGRAM \n") 
print(n_gram)
print("\n\n\n")

###---------------------tfidf-----------------------------------------------------------###

def doc_with_terms(bag_words):
    doc_with_the_term = {}
    
    for file in bag_words:
        for word in bag_words[file]:
            if not word in doc_with_the_term.keys():
                doc_with_the_term[word] = 1
            else:
                doc_with_the_term[word] = doc_with_the_term[word] + 1
    
    return doc_with_the_term

def find_total(tokens):
    total = 0
    for key in tokens:
        total = total + tokens[key]
    return total

def find_tfidf (tokens, idf_dict):
    total = find_total(tokens)
    tfidf_dict = {}
    
    for word in tokens:
        tfidf_dict[word] = (tokens[word]/total)*(1 + math.log(len(files_paths)/idf_dict[word]))
    print(tfidf_dict)
    return tfidf_dict

idf_dict = doc_with_terms(bag_words)

tfidf_final = {}                                                 
for entry in bag_words:
    tfidf_final[entry] = find_tfidf(bag_words[entry], idf_dict)
                                                 
print(tfidf_final)
print("\n\n\n")

###---------------------re-representing data-----------------------------------------------------------###

keys = tfidf_final.keys()
keys = sorted(keys)
print(keys)

word_tfidf_dict = {}
word_list = []

for key in tokenized:
    for word in tokenized[key]:
        if not word in word_list:
            word_list.append(word)

print("ALL WORDS")
print(word_list)
print("\n\n\n")

for word in word_list:
    local_list = []
    for key in keys:
        if word in tfidf_final[key]:
            local_list.append(tfidf_final[key][word])
        else:
            local_list.append(0)
    word_tfidf_dict[word] = local_list

print("RE-REPRESENTED DATA")
print(word_tfidf_dict)
print("\n\n\n")

###---------------------cosine similarity-----------------------------------------------------------###
###---Cosine Similarity(Query,Document1) = Dot product(Query, Document1) / ||Query|| * ||Document1||---###

cosine_similarity_dict = {}
glob_count = 0
for key in bag_words:
    magnitude_this = 0
    dot_product = 0
    local_dot_array = [0] * len(files_paths)
    local_mag_array = [0] * len(files_paths)
    
    for word in word_tfidf_dict:
        count = 0
        
        for number in word_tfidf_dict[word]:
            dot_product = word_tfidf_dict[word][glob_count] * number
            local_dot_array[count] = local_dot_array[count] + dot_product
            local_mag_array[count] = local_mag_array[count] + number*number
            count = count + 1
    
    final_sim_array = [0] * len(files_paths)
    
    for i in range(0,len(files_paths)):
        final_sim_array[i] = local_dot_array[i]/(math.sqrt(local_mag_array[i]) * math.sqrt(local_mag_array[glob_count]))
    
    cosine_similarity_dict[key] = final_sim_array
    glob_count = glob_count + 1

print("SIMILARITY DICTIONARY")
print(cosine_similarity_dict)
print("\n\n\n")   

###---------------------represent as 2D array-----------------------------------------------------------###

twoD = [[0 for x in range(len(files_paths))] for x in range(len(files_paths))] 
count = 0
for key in cosine_similarity_dict:
    for i in range(0,len(files_paths)):
        twoD[count][i] = (cosine_similarity_dict[key][i])
    count = count + 1

print("2D representation")
print(twoD)
print("\n\n\n")   

###---------------------DATA VISUALIZATION-----------------------------------------------------------###

import matplotlib.pyplot as plt
import numpy as np

plt.imshow(twoD, cmap='hot', interpolation='nearest')
plt.show()

print("Heat Map of Similarity, lighter is more alike\n")
print("Here is raw data:\n")
print(twoD)
print("\n\n\n")   