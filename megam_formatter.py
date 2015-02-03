#this is to convert a file generated from readfiles.py into MegaM format
#takes 2 arguments 1.input file which is generated output of the readfiles.py 2.output filename

import re
import codecs
import sys


def main():
    
    #usage details
    if len(sys.argv) < 3:
        print("Usage : python3 megam_formatter.py input_filename output_filename")
        return
    
    #open input file
    input_file = open(sys.argv[1], 'r', encoding = 'latin-1',errors='ignore')
    #MegaM format file
    output_file = open(sys.argv[2] , 'w+', encoding = 'latin-1', errors = 'ignore')
     
    for line in input_file:
        mega_line = ""
        word_count = {}
        feature_vector = {}
        words = re.split(r'\s+', line.replace('#','#_').rstrip()) #pound symbol was leading to exception in megam learn, therefore replacing
        if words[0] == 'HAM' or words[0] == 'POS':
            mega_line = '1\t'
            n = 1
        elif words[0]== 'SPAM' or words[0] == 'NEG':
            mega_line = '0\t'        
            n = 1
        else:
            mega_line = '0\t'
            n = 0
        #calculating counts for each word    
        for word in words[n:]:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            
        #MegaM non bernoulli format class_label (feature_name feature_value)
        for word in sorted(word_count):
            mega_line += str(word)+ ' ' + str(word_count[word])+' '
            
##        for word in words[1:]:
##            mega_line += str(word)+ ' '
        
        #write each line to output file    
        output_file.write(mega_line.rstrip() + '\n')
        
        
    #close the files
    input_file.close()
    output_file.close()
    
    return
    

#boilerplate for main
if __name__ == '__main__':
    main()