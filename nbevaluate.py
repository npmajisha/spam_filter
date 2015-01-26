#this is to evaluate the performance of the nbclassifier
# precision - count(correctly classified as class)/count(classified as class)
# recall - count(correctly classified as class)/count(actually belonging to class)
#f1 score = 2*precision*recall/ precision + recall
import sys
import re

def main():
    
    output_file = open(sys.argv[1],'r+')
    
    words = []
    # act - actual count of documents in a class
    # corr - count of documents that were correctly identified as belonging to a class
    # class - count of documents that were classified as belonging to a class
    act_ham_count = 0
    act_spam_count = 0
    act_pos_count = 0
    act_neg_count = 0
    corr_spam_count = 0
    corr_ham_count = 0
    corr_pos_count = 0
    corr_neg_count = 0
    class_spam = 0
    class_ham = 0
    class_pos = 0
    class_neg = 0
    
    for line in output_file:
        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
        if words[0].startswith('HAM'):
            act_ham_count += 1
            if words[1]=='HAM':
                corr_ham_count += 1
                class_ham += 1
            else:
                class_spam += 1
        elif words[0].startswith('SPAM'):
            act_spam_count += 1
            if words[1] == 'SPAM':
                corr_spam_count += 1
                class_spam += 1
            else:
                class_ham += 1
        elif words[0].startswith('POS'):
            act_pos_count +=1
            if words[1] == 'POS':
                corr_pos_count +=1
                class_pos +=1
            else:
                class_neg +=1
        elif words[0].startswith('NEG'):
            act_neg_count +=1
            if words[1] == 'NEG':
                corr_neg_count +=1
                class_neg +=1
            else:
                class_pos +=1
    if class_ham!=0 and class_spam!=0:
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
        print('F1 score HAM' ,f1_score)
        f1_score = (2*precision_spam *recall_spam)/(precision_spam +recall_spam)
        print('F1 score SPAM',f1_score)
    
    if class_pos!=0 and class_neg!=0:
        precision_pos = float(corr_pos_count/class_pos)
        print('Precision pos',precision_pos*100)
        precision_neg = float(corr_neg_count/class_neg)
        print('Precision neg', precision_neg*100)

        recall_pos = float(corr_pos_count/act_pos_count)
        print('Recall pos', recall_pos*100)
        recall_neg = float(corr_neg_count/act_neg_count)
        print('Recall neg',recall_neg*100)
    
        f1_score = 0.0
        f1_score = (2 * precision_pos * recall_pos)/(precision_pos + recall_pos)
        print('F1 score POS' ,f1_score)
        f1_score = (2*precision_neg*recall_neg)/(precision_neg + recall_neg)
        print('F1 score NEG', f1_score)


#boilerplate for main
if __name__ == '__main__':
    main()