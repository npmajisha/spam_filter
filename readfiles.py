#this program is to read all files in the directory and create the training file

import os
import string

#add label based on the filename
def add_label(filename):
    if filename.startswith('HAM'):
        return 'HAM '
    else:
        return 'SPAM '

#ignoring punctuation marks
def remove_punctuation(line):
    new_line = ""
    for char in line:
        if char in string.punctuation:
            new_line += ' '
        else:
            new_line += char
    return new_line


def main():

    o_file = open("spam_training.txt", 'w')
    feature_list = ""
    
    for root , dirs , files in os.walk(".",topdown=False):
        for filename in files:
            if filename.startswith('HAM') or filename.startswith('SPAM'):
                i_file = open(filename,'r')
                feature_list = add_label(filename) #add label 'HAM' or 'SPAM'
                for line in i_file:                    
                    feature_list += remove_punctuation(line).rstrip() + ' '

                o_file.write(feature_list + '\n')
                i_file.close()

    o_file.close()












#boilerplate for main
if __name__ == '__main__':
    main()
