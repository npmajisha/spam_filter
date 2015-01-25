#this program is to read all the training set files in the directory and create the training file

import os
import string
import re
import sys

#add label based on the filename
def add_label(filename):
    if filename.startswith('HAM'):
        return 'HAM '
    elif filename.startswith('SPAM'):
        return 'SPAM '
    elif filename.startswith('POS'):
        return 'POS'
    elif filename.startswith('NEG'):
        return 'NEG'

#ignoring punctuation marks
def remove_punctuation(line):
    words = []
    words = re.findall(r"\w+|[^\w\s]",line.rstrip()) #regular expression to split on non-word characters
  
    new_line = ' '.join(words)

    return new_line + ' '


def main():

    o_file = open("spam_training.txt", 'w')
    feature_list = ""
    print(sys.argv[1])
    for root , dirs , files in os.walk('./'+sys.argv[1],topdown=False):

        for filename in files:
            if filename.endswith('.txt'):
                i_file = open('./'+sys.argv[1]+'/'+filename,'r' , encoding = 'latin-1')
                feature_list = add_label(filename) #add label 'HAM' or 'SPAM'
                for line in i_file:                    
                    feature_list += remove_punctuation(line.lower())
                    
                o_file.write(feature_list + '\n')
                
                i_file.close()

    o_file.close()


#boilerplate for main
if __name__ == '__main__':
    main()
