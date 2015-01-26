#this is to evaluate the performance of the nbclassifier

import sys
import re

def main():
    
    output_file = open(sys.argv[1],'r+')
    
    words = []
    act_ham_count = 0
    act_spam_count = 0
    corr_spam_count = 0
    corr_ham_count = 0
    class_spam = 0
    class_ham = 0
    
    for line in output_file:
        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
        if words[0].startswith('HAM'):
            act_ham_count += 1
            if words[1]=='HAM':
                corr_ham_count += 1
                class_ham += 1
            else:
                class_spam += 1
        else:
            act_spam_count += 1
            if words[1] == 'SPAM':
                corr_spam_count += 1
                class_spam += 1
            else:
                class_ham += 1

    precision_ham = float(corr_ham_count/class_ham)
    print('Precision ham',precision_ham*100)
    precision_spam = float(corr_spam_count/class_spam)
    print('Precision spam', precision_spam*100)
    recall_ham = float(corr_ham_count/act_ham_count)
    print('Recall ham', recall_ham*100)
    recall_spam = float(corr_spam_count/act_spam_count)
    print('Recall spam',recall_spam*100)
    
    f1_score = 0.0
    f1_score = (2 * precision_ham * recall_ham)/(precision_ham + recall_ham)
    print('F1 score' ,f1_score)
        


#boilerplate for main
if __name__ == '__main__':
    main()