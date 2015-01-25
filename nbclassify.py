#this program is to classify input files by using the model file that is built

import sys
import re

def xml_parser(line):
	tags = []
	tags = re.split(r'\s+',line)
    return tags

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
    model_file = open(sys.argv[2],'r+')
    i=0
    classes = []
    lines = model_file.readlines()
    classes = re.split(r'\s+' , lines[0].rstrip())
    class_vocab_count = {} #dictionary to store a tuple ( N,k) here N is the total number of words and k is the number of unique words

    class_vocab_map = {} #dictionary to store the vocabulary of each 
	
    for label in classes:
        vocab = {}
        class_vocab_map[label] = vocab
        class_vocab_count[label]= (0,0)
	
    label = ''
    words = []
    dict = {}
	
    for line in lines[1:]:
        words = xml_parser(line)
        print(words)
        if len(words) == 3: #case of open tags
            label = words[0]
            print(words)
            class_vocab_count[label] = (int(words[1]),int(words[2]))
        elif len(words) == 2: #element tags
            dict = class_vocab_map[label]
            dict[words[0]] = int(words[1])
    
    print(class_vocab_count['HAM'])
    



#boilerplate for main

if __name__ == '__main__':
    main()
