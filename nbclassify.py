#this program is to classify input files by using the model file that is built

import sys
import re
import codecs
import math

class Training_model:
    def __init__(self,class_list,class_priors, count_map , vocab_map):
        self.count_map = count_map
        self.vocab_map = vocab_map
        self.class_list = class_list
        self.class_prior = class_priors
    
    
    def get_class_vocab_count(self,label):
        return self.count_map[label]
     
    def get_class_vocab(self, label):
        return self.vocab_map[label]
    
    def get_N_and_k(self,label):
        count_tuple= ()
        count_tuple = self.count_map[label]
        return count_tuple
    
    def get_prior(self,label):
        return self.class_prior[label]
    
    def get_labels(self):
        return self.class_list
        

def classify(t_model,words):
    
    #get the available classes
    classes = []
    classes = t_model.get_labels()
    prob_doc_class = []
    max=0.0
    label_classified = ''
    for label in classes: #calculare P(c|d) = P(c) * P(d|c) = P(c) * P(w1|c) * P(w2|c) ... P(wn|c)
        print(label)
        p_c_given_d = 0.0
        p_d_given_c = 0.0
        prior_c = math.log(t_model.get_prior(label))
        print(str(prior_c))
        class_vocab = {}
        class_vocab = t_model.get_class_vocab(label)
        class_vocab_count = ()
        class_vocab_count = t_model.get_class_vocab_count(label)
        
        for word in words:
            if word in class_vocab:
                p_d_given_c += math.log(float(class_vocab[word]/class_vocab_count[1]))
            else:
                p_d_given_c += math.log(float(1/(class_vocab_count[0]+class_vocab_count[1])))
        
        p_c_given_d = prior_c + p_d_given_c
        prob_doc_class.append((p_c_given_d,label))
            
    return  ((sorted(prob_doc_class, reverse=True)[0])[1])
    
        
        

def xml_parser(line):
    tags = []
    tags = re.split(r'\s+',line)
    return tags[1:-2]   
    
    

def main():
    
    
    #read the model file and build a dictionary
    model_file = codecs.open(sys.argv[1],'r+', 'utf-8',errors='ignore')
    output_file = open("output.txt",'w+')
    header = []
    lines = model_file.readlines()
    header = re.split(r'\s+' , lines[0].rstrip())
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
    for line in lines[1:]:
        words = xml_parser(line)        
        if len(words) == 3: #case of open tags
            label = words[0]
            class_vocab_count[label] = (int(words[1]),int(words[2]))
        elif len(words) == 2: #element tags
            dict = class_vocab_map[label]
            dict[words[0]] = int(words[1])
    
    training_model = Training_model(classes,class_priors,class_vocab_count,class_vocab_map)
    #print(training_model.get_labels())
    model_file.close()
    #output_file = codecs.open("output.txt" ,'w+', 'utf-8',errors='ignore')
    
    
    #take the input file which has to be classified
    #each line is a document. Split each line on the basis of spaces
    #print("Opening test file")
    test_file = codecs.open(sys.argv[2],'r+','utf-8',errors='ignore')
    #print("File opened successfully")
    label = ''
    log= ''
    for line in test_file:
        words = []
        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
        label = classify(training_model,words[1:]) #call the classify method passing the training model
        #print(words[0],label)
        log = words[0] +' '+ label
        output_file.write(log+'\n')
    
    output_file.close()
    test_file.close()
    return

#boilerplate for main

if __name__ == '__main__':
    main()
