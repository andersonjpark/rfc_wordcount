from numba import njit
import os
import re
import collections

# @njit
def word_normalizer(clean_counter, dirty_sentence):
    """ Input : counter, un-normalized sentence
        Output: counter
        Description: This function takes a unnormalized sentence, normalize it,
        and update given counter by feeding words tokens.
        """
    sub_sentence = re.sub(r"[^a-zA-Z0-9]", '\t', dirty_sentence)
    upper_sentence = sub_sentence.upper()
    clean_list = upper_sentence.split()  # Returns list that contains words of sentence
    clean_counter.update(clean_list)
    return clean_counter

def execution_f(root_dir):
    """ Input : List
        Output: Counter
        Description: This function will take a list of all file directories, open
        each file and collect the body content. Then it will normalize all the
        text in the body content and return the counter with word tokens."""
    clean_counter = collections.Counter()

    for root, dirs, files in os.walk(root_dir):  # os.walk doesn't have disregarding hidden files or dirs
        files = [f for f in files if not f[0] == '.']  # Disregard Hidden files
        dirs[:] = [d for d in dirs if not d[0] == '.']  # Disregard hidden dirs
        for filename in files:
            with open(os.path.join(root, filename), 'r', encoding="latin-1", newline='') as openFile:
                while True:  # Removing the header of email
                    header = openFile.readline()
                    if header == '\r\n':
                        break
                dirty_file = openFile.read() # Feeding total body
                clean_counter = word_normalizer(clean_counter, dirty_file)
    return clean_counter

def print_dict(clean_counter):
    """ Input : Counter
        Output:
        Description: This function will take a dictionary, sort it in descending
        order and print the frequency and word."""
    sorted_list = clean_counter.most_common()  # Organizing the dictionary in descending order
    for (word, frequency) in sorted_list:
        print(f'{frequency} {word}')

def writeDict(cleanCounter):
    sortedList = cleanCounter.most_common()
    with open('output/single_outputFile.txt', "w") as outputFile:
        for (word, frequency) in sortedList:
            outputFile.write(str(frequency)+" ")
            outputFile.write(word)
            outputFile.write("\n")
        outputFile.close()
