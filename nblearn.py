#Naive Bayes Classifier
#this code is to learn from the training file(input argument)
#and develop a learning model that will be saved in a model 
#file (input argument) 
import sys
import re
import codecs

def main():
    
    #usage details
    if len(sys.argv) < 2:
        print("Usage : python3 nblearn.py training_file model_file")
        exit(0)

	
	#open training file
    training_file = codecs.open(sys.argv[1], 'r', 'utf-8',errors='ignore')
    model_file = codecs.open(sys.argv[2], 'w' , 'utf-8',errors='ignore')	
    
    common_dictionary = {}
    class_vocab_map = {} #a dictionary to store class and the corresponding vocabulary
    class_docs = {} #dictionary to store class and documents count
    classes = []
    words = []
    
    
    #total_number_of_documents
    tot_docs = 0
    for line in training_file:
        tot_docs += 1
        vocab = {} #a dictionary to store the word and corresponding counts
        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
        
        if words[0] not in class_vocab_map:
            class_docs[words[0]]=1
            class_vocab_map[words[0]] = vocab
        else:
            class_docs[words[0]] = class_docs[words[0]]+1
            vocab = class_vocab_map[words[0]]
        
        for word in words[1:]:
            if word not in vocab:
                vocab[word] = 1
            else:
                vocab[word] = vocab[word] + 1
                
            if word not in common_dictionary:
                common_dictionary[word] = 1
        
						
		
	
    #constructing the xml elements
    log = ""
    header = ""
    total_vocab_size = len(common_dictionary)
    for key in class_vocab_map:
        inner_element = ""
        
        open_tag = ""
        lose_tag = ""
        total_words = 0
        classes.append(key)
        
        #header is for e.g. HAM HAM_prior SPAM SPAM_prior
        header += key + ' ' + str(float(class_docs[key]/tot_docs)) + ' '
        vocabulary = class_vocab_map[key]
        
        #open tag for each class < HAM unique_vocabulary_size total_words >
        open_tag += '< ' + key + ' ' + str(len(vocabulary)) + ' '
		
        #for each item tag e.g. < word count_of_occurrences >
        for item in sorted(vocabulary.keys()):
            inner_element += '< ' + item + ' ' + str(vocabulary[item])  + ' />' + '\n'
            total_words += vocabulary[item]
            
        open_tag += str(total_words) + ' >' + '\n'
        
        #close tag for class e.g.</ HAM>
        close_tag = '</ ' + key + ' >'+ '\n'
        
        log+= open_tag + inner_element + close_tag
        
    #close the training file    
    training_file.close()
    
    #write to the model file
    model_file.write(str( header + '\n'))
    model_file.write("vocab_size"+' '+ str(total_vocab_size)+'\n')
    model_file.write(log)    
    model_file.close()
    return


#boilerplate for main
if __name__ == '__main__':
	main()
