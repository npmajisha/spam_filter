#this program is to read all the training set files in the directory and create the training file
#accepts two arguments 1.Directory containing the training/dev set files 2.the training/dev output file name

import os
import string
import re
import sys
import codecs

#add label based on the filename
def add_label(filename):
    if filename.startswith('HAM'):
        return 'HAM '
    elif filename.startswith('SPAM'):
        return 'SPAM '
    elif filename.startswith('POS'):
        return 'POS '
    elif filename.startswith('NEG'):
        return 'NEG '


#keeping punctuations
def tokenize(line):
    words = []
    words = re.findall(r"\w+|[^\w\s]",line.rstrip()) #regular expression to split on non-word characters
    new_line = ' '.join(words)

    return new_line + ' '


def main():
    
    #usage details
    if len(sys.argv) < 4:
        print("Usage : python3 readfiles.py --test/train /path/to/directory output_filename")
        exit(0)
    
    #output file of the format class_label feature1 feature2...featurnN
    o_file = codecs.open(sys.argv[3], 'w+', 'utf-8')
    
    feature_list = ""
 
    for root , dirs , files in os.walk('./'+sys.argv[2],topdown=False):

        for filename in sorted(files): #sort the files to preserve order
            if filename.endswith('.txt'):
                i_file = codecs.open('./'+sys.argv[2]+'/'+filename,'r+' , 'utf-8', errors='ignore')
                if sys.argv[1]=='--train':
                    feature_list = add_label(filename) #add class label 'HAM'/'SPAM' or 'POS/NEG'
                elif sys.argv[1] =='--test':
                    feature_list = ''
                #build feature_list by concatenating all the tokens            
                for line in i_file:                    
                    feature_list += tokenize(line.lower())
                
                #single line for each document
                o_file.write(feature_list+'\n')
                
                #close the input file
                i_file.close()           
    
        
    #close the output file    
    o_file.close()
    return


#boilerplate for main
if __name__ == '__main__':
    main()
    
