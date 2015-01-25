#this program is to classify input files by using the model file that is built

import sys
import re

def extract_words(filename):
    f = open(filename , 'r')
    words = []
    for line in f:
        words.extend(re.findall(r"\w+|[^\w\s]",(line.lower()).rstrip()))
    return words
        

def main():
    
    #take the input file which has to be classified
    words_from_input = []
    words_from_input = extract_words(sys.argv[1])
    
    #read the model file and build a dictionary









#boilerplate for main

if __name__ == '__main__':
    main()
