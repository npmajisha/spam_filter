#this is to evaluate the performance of the nbclassifier
# precision - count(correctly classified as class)/count(classified as class)
# recall - count(correctly classified as class)/count(actually belonging to class)
#f1 score = 2*precision*recall/ precision + recall
import sys
import re
import os

def main():
    
    words = []
    # act - actual count of documents in a class
    # corr - count of documents that were correctly identified as belonging to a class
    # class - count of documents that were classified as belonging to a class
    act_ham_count = 0
    act_spam_count = 0
    act_pos_count = 0
    act_neg_count = 0
    #index 0 is for Naive Bayes , index 1 for SVM_Light, index 2 for MegaM
    corr_spam_count = []
    corr_ham_count = []
    corr_pos_count = []
    corr_neg_count = []
    class_spam = []
    class_ham = []
    class_pos = []
    class_neg = []
    
    for i in range(3):
        corr_ham_count.append(0)
        corr_spam_count.append(0)
        class_ham.append(0)
        class_spam.append(0)
        corr_pos_count.append(0)
        corr_neg_count.append(0)
        class_neg.append(0)
        class_pos.append(0)
    if sys.argv[1] == '--spam':
        spam_out = open("spam.dev.out",'r+')
        svm_spam_out = open(os.path.join("./svm_light","spam.dev.svm.out"),'r+')
        megam_spam_out = open(os.path.join("./MEGAM","spam.dev.megam.out"),'r+')
    else:
        sentiment_out = open("sentiment.dev.out",'r+')
        svm_sent_out = open(os.path.join("./svm_light","sentiment.dev.svm.out"),'r+')
        megam_sent_out = open(os.path.join("./MEGAM","sentiment.dev.megam.out"),'r+')

    for root , dirs , files in os.walk('./'+sys.argv[2],topdown=False):

        for filename in sorted(files):
            if sys.argv[1] == '--spam':
                
                nb_out = spam_out.readline().rstrip()
                svm_out = svm_spam_out.readline().rstrip()
                megam_out = megam_spam_out.readline().rstrip()

            else:
                nb_out = sentiment_out.readline().rstrip()
                svm_out = svm_sent_out.readline().rstrip()
                megam_out = megam_sent_out.readline().rstrip()
                
            if filename.startswith('HAM'):
                act_ham_count +=1               
                
                if nb_out == 'HAM':
                    corr_ham_count[0] +=1
                    class_ham[0] += 1
                elif nb_out == 'SPAM':
                    class_spam[0] +=1
                    
                if svm_out == 'HAM':
                    corr_ham_count[1] +=1
                    class_ham[1] += 1
                elif svm_out == 'SPAM':
                    class_spam[1] +=1
                    
                if megam_out == 'HAM':
                    corr_ham_count[2] +=1
                    class_ham[2] += 1
                elif nb_out == 'SPAM':
                    class_spam[2] +=1
                    
            elif filename.startswith('SPAM'):
                act_spam_count +=1
                
                if nb_out == 'SPAM':
                    corr_spam_count[0] += 1
                    class_spam[0] += 1
                elif nb_out == 'HAM':
                    class_ham[0] += 1
                
                if svm_out == 'SPAM':
                    corr_spam_count[1] +=1
                    class_spam[1] += 1
                elif svm_out == 'HAM':
                    class_ham[1] +=1
                    
                if megam_out == 'SPAM':
                    corr_spam_count[2] +=1
                    class_spam[2] += 1
                elif nb_out == 'HAM':
                    class_ham[2] +=1
    
            
            if filename.startswith('POS'):
                act_pos_count +=1               
                
                if nb_out == 'POS':
                    corr_pos_count[0] +=1
                    class_pos[0] += 1
                elif nb_out == 'NEG':
                    class_neg[0] +=1
                    
                if svm_out == 'POS':
                    corr_pos_count[1] +=1
                    class_pos[1] += 1
                elif svm_out == 'NEG':
                    class_neg[1] +=1
                    
                if megam_out == 'POS':
                    corr_pos_count[2] +=1
                    class_pos[2] += 1
                elif megam_out == 'NEG':
                    class_neg[2] +=1
                    
            elif filename.startswith('NEG'):
                act_neg_count +=1
                
                if nb_out == 'NEG':
                    corr_neg_count[0] += 1
                    class_neg[0] += 1
                elif nb_out == 'POS':
                    class_pos[0] += 1
                
                if svm_out == 'NEG':
                    corr_neg_count[1] +=1
                    class_neg[1] += 1
                elif svm_out == 'POS':
                    class_pos[1] +=1
                    
                if megam_out == 'NEG':
                    corr_neg_count[2] +=1
                    class_neg[2] += 1
                elif megam_out == 'POS':
                    class_pos[2] +=1
                    
    
##    for line in output_file:
##        words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
##        if words[0].startswith('HAM'):
##            act_ham_count += 1
##            if words[1]=='HAM':
##                corr_ham_count += 1
##                class_ham += 1
##            else:
##                class_spam += 1
##        elif words[0].startswith('SPAM'):
##            act_spam_count += 1
##            if words[1] == 'SPAM':
##                corr_spam_count += 1
##                class_spam += 1
##            else:
##                class_ham += 1
##        elif words[0].startswith('POS'):
##            act_pos_count +=1
##            if words[1] == 'POS':
##                corr_pos_count +=1
##                class_pos +=1
##            else:
##                class_neg +=1
##        elif words[0].startswith('NEG'):
##            act_neg_count +=1
##            if words[1] == 'NEG':
##                corr_neg_count +=1
##                class_neg +=1
##            else:
##                class_pos +=1

    for i in range(3):
        if i == 0:
            print("Naive Bayes")
        elif i == 1:
            print("SVM_Light")
        elif i == 2:
            print("MegaM Light")
            
        if class_ham[i]!=0 and class_spam[i]!=0:
            precision_ham = float(corr_ham_count[i]/class_ham[i])
            
            print('Precision ham',precision_ham*100)
            precision_spam = float(corr_spam_count[i]/class_spam[i])
            print('Precision spam', precision_spam*100)

            recall_ham = float(corr_ham_count[i]/act_ham_count)
            print('Recall ham', recall_ham*100)
            recall_spam = float(corr_spam_count[i]/act_spam_count)
            print('Recall spam',recall_spam*100)
        
            f1_score = 0.0
            f1_score = (2 * precision_ham * recall_ham)/(precision_ham + recall_ham)
            print('F1 score HAM' ,f1_score)
            f1_score = (2*precision_spam *recall_spam)/(precision_spam +recall_spam)
            print('F1 score SPAM',f1_score)
        
        
        if class_pos[i]!=0 and class_neg[i]!=0:
            precision_pos = float(corr_pos_count[i]/class_pos[i])
            print('Precision pos',precision_pos*100)
            precision_neg = float(corr_neg_count[i]/class_neg[i])
            print('Precision neg', precision_neg*100)

            recall_pos = float(corr_pos_count[i]/act_pos_count)
            print('Recall pos', recall_pos*100)
            recall_neg = float(corr_neg_count[i]/act_neg_count)
            print('Recall neg',recall_neg*100)
        
            f1_score = 0.0
            f1_score = (2 * precision_pos * recall_pos)/(precision_pos + recall_pos)
            print('F1 score POS' ,f1_score)
            f1_score = (2*precision_neg*recall_neg)/(precision_neg + recall_neg)
            print('F1 score NEG', f1_score)


#boilerplate for main
if __name__ == '__main__':
    main()
