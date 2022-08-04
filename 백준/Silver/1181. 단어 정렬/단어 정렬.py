import sys

#N = int(sys.stdin.readline().rstrip())

N= int(input())

dictionary = {}

for i in range(N):

    word = input()

    dictionary[word] = len(word)

    

dictionary_by_length = {}

for key, value in dictionary.items():

    if dictionary_by_length.get(value):

        dictionary_by_length[value].append(key)

    else:
        dictionary_by_length[value]=[key]
        
dictionary_by_length = sorted(dictionary_by_length.items())

for idx, words in dictionary_by_length:
    for word in sorted(words):
        print(word)