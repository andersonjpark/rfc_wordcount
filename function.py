
import os
import re
import collections

def word_normalizer(dirty_sentence: str) -> list:
    """ Input : counter, un-normalized sentence
        Output: list
        Description: This function takes a unnormalized sentence, normalize it,
        and update given counter by feeding words tokens.
        """
    sub_sentence = re.sub(r"[^a-zA-Z0-9]", '\t', dirty_sentence)
    upper_sentence = sub_sentence.upper()
    clean_list = upper_sentence.split()  # Returns list that contains words of sentence
    return clean_list

def get_file_paths(root_dir: str) -> list:
    """ Input : directory
        Output: list
        Description: This function will generate the file names in a directory
        tree by walking the tree top-down.
    """ 
    path_list = [] # List which will store all of the full filepaths.
    # Walk the tree.
    for root, dirs, files in os.walk(root_dir):  # os.walk doesn't have disregarding hidden files or dirs
        files = [f for f in files if not f[0] == '.']  # Disregard Hidden files
        dirs[:] = [d for d in dirs if not d[0] == '.']  # Disregard hidden dirs
        for filename in files:
            # Join two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            path_list.append(filepath) # Append to list.
    return path_list

def execution_f(path_list: list) -> collections.Counter:
    """ Input : List
        Output: Counter
        Description: This function will take a list of all file directories, open
        each file and collect the body content. Then it will normalize all the
        text in the body content and return the counter with word tokens."""
    print("start process")
    clean_counter = collections.Counter()
    for path in path_list:
        with open(path, 'r', encoding="latin-1", newline='') as openFile:
            while True:  # Removing the header of email
                dirty_sentence = openFile.readline()
                if dirty_sentence == '\r\n':
                    break
            dirty_file = openFile.read() # Feeding total body
            clean_counter.update(word_normalizer(dirty_file))
    print('end process')
    return clean_counter

def print_dict(clean_counter):
    """ Input : Counter
        Output:
        Description: This function will take a dictionary, sort it in descending
        order and print the frequency and word."""
    sorted_list = clean_counter.most_common()  # Organizing the dictionary in descending order
    for (word, frequency) in sorted_list:
        # print('{} {}'.format(frequency, word))
        print(f'{frequency} {word}')

def writeDict(cleanCounter):
    sortedList = cleanCounter.most_common()
    with open('output/multi_outputFile.txt', "w") as outputFile:
        for (word, frequency) in sortedList:
            outputFile.write(str(frequency)+" ")
            outputFile.write(word)
            outputFile.write("\n")
        outputFile.close()
