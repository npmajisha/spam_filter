#this program is to classify input files by using the model file that is built
#usage : python3 nbclassify.py model_file test_file

import sys
import re
import codecs
import math

#class to store the training model read from the model_file
class Training_model:
    def __init__(self,class_list,total_vocab_size,class_priors, count_map , vocab_map):
        self.count_map = count_map 
        self.vocab_map = vocab_map
        self.class_list = class_list
        self.class_prior = class_priors
        self.total_vocab_size = total_vocab_size
    
    def get_class_vocab_count(self,label):
        return self.count_map[label]
     
    def get_class_vocab(self, label):
        return self.vocab_map[label]
    
    def get_k_vocab_size(self):
##        count_tuple = ()
##        k = 0
##        #count_tuple[0] contains the unique number of words in the corresponding class
##        for key in self.count_map:
##            count_tuple = self.count_map[key]
##            k += count_tuple[0]
##        
##        return k
        return self.total_vocab_size
    
    def get_prior(self,label):
        return self.class_prior[label]
    
    def get_labels(self):
        return self.class_list
        

def classify(t_model,words):
    
    #get the available classes
    classes = []
    classes = t_model.get_labels()
    
    prob_doc_class = []
    for label in classes: #calculate P(c|d) = P(c) * P(d|c) = P(c) * P(w1|c) * P(w2|c) ... P(wn|c)
        p_c_given_d = 0.0
        p_d_given_c = 0.0
        prior_c = math.log(t_model.get_prior(label))
        class_vocab = {}
        class_vocab = t_model.get_class_vocab(label)
        class_vocab_count = ()
        class_vocab_count = t_model.get_class_vocab_count(label)       
        #get the vocab size of the model
        total_vocab_size = t_model.get_k_vocab_size()
        
        #add one smoothing
        #P(word|c) = count(word,c)+1 / N(:total no of words in the class) + k(:total vocab size)
        for word in words:
            if word in class_vocab:
                p_d_given_c += math.log((class_vocab[word]+1)/(class_vocab_count[1]+total_vocab_size+1))
            else:
                #for unknown words just keeping 1 in the numerator
                p_d_given_c += math.log(1/(class_vocab_count[1]+total_vocab_size+1))
        
        p_c_given_d = prior_c + p_d_given_c
        prob_doc_class.append((p_c_given_d,label)) 
         
    return  ((sorted(prob_doc_class, reverse=True)[0])[1])
    
        
        

def xml_parser(line):
    tags = []
    tags = re.split(r'\s+',line)
    return tags[1:-2]   
    
    

def main():
    
    if len(sys.argv) < 3:
        print("Usage: python3 nbclassify.py model_file test_file > output_filename")
        return
    
    
    #read the model file and build a dictionary
    model_file = codecs.open(sys.argv[1],'r+', 'utf-8',errors='ignore')
        
    header = []
    lines = model_file.readlines()
    header = re.split(r'\s+' , lines[0].rstrip())
    total_vocab_size = int(re.split(r'\s+',lines[1].rstrip())[1])
    class_vocab_count = {} #dictionary to store a tuple (k,N) here N is the total number of words and k is the number of unique words
    class_priors = {}
    class_vocab_map = {} #dictionary to store the vocabulary of each 
	
    i=0
    classes = []
    while(i < len(header)):
        label = header[i]
        classes.append(label)
        prior = float(header[i+1])
        class_priors[label]=prior
        vocab = {}
        class_vocab_map[label] = vocab
        class_vocab_count[label]= (0,0)
        i += 2
	
    label = ''
    words = []
    dict = {}
    
    for line in lines[2:]:
        words = xml_parser(line)  
        if len(words) == 3: #open tags for classes
            label = words[0]
            class_vocab_count[label] = (int(words[1]),int(words[2]))
        elif len(words) == 2: #element tags
            dict = class_vocab_map[label]
            dict[words[0]] = int(words[1])
    
    training_model = Training_model(classes,total_vocab_size,class_priors,class_vocab_count,class_vocab_map)
    #print(training_model.get_labels())
    model_file.close()
    
    
    #take the input file which has to be classified
    #each line is a document. Split each line on the basis of spaces
    #print("Opening test file")
    test_file = codecs.open(sys.argv[2],'r+','utf-8',errors='ignore')

    label = ''
    for line in test_file:
        words = []
        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
        label = classify(training_model,words) #call the classify method passing the training model
        #print(words[0],label)
        #write classified label to output file
        print(label)
    
    
    test_file.close()
    return

#boilerplate for main

if __name__ == '__main__':
    main()
