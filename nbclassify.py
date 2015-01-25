#this program is to classify input files by using the model file that is built

import sys
import re
import codecs

class Training_model:
    def __init__(self,class_list, count_map , vocab_map):
        self.count_map = count_map
        self.vocab_map = vocab_map
        self.class_list = class_list
    
    def add_one_smoothing(self , label , word ):
        vocab = {}
        vocab = self.vocab_map[label]
        return vocab[word]+1
    
    def get_N_and_k(label):
        count_tuple= ()
        count_tuple = self.count_map[label]
        return count_tuple
    
    def get_labels(self):
        return self.class_list
        

def classify(t_model,words):
    
    #get the available classes
    classes = []
    classes = t_model.get_labels()
    
    for label in classes:
        

def xml_parser(line):
    tags = []
    tags = re.split(r'\s+',line)
    return tags[1:-2]   
    
    

def main():
    
    
    #read the model file and build a dictionary
    model_file = codecs.open(sys.argv[1],'r+', 'utf-8',errors='ignore')
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
        if len(words) == 3: #case of open tags
            label = words[0]
            class_vocab_count[label] = (int(words[1]),int(words[2]))
        elif len(words) == 2: #element tags
            dict = class_vocab_map[label]
            dict[words[0]] = int(words[1])
    
    print(class_vocab_count['HAM'])
    print(class_vocab_count['SPAM'])
    
    training_model = Training_model(classes,class_vocab_count,class_vocab_map)
    print(training_model.get_labels())
    output_file = codecs.open("output.txt" ,'w+', 'utf-8',errors='ignore')
    
    
    #take the input file which has to be classified
    #each line is a document. Split each line on the basis of spaces
    test_file = codecs.open(sys.argv[1],'r+','utf-8',errors='ignore')
    
    label = ''
    for line in test_file:
        words = []
        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
        label = classify(training_model,words) #call the classify method passing the training model


#boilerplate for main

if __name__ == '__main__':
    main()
