Part 3
SPAM
Naive Bayes
Precision ham 98.79518072289156
Precision spam 95.64032697547684
Recall ham 98.4
Recall spam 96.69421487603306
F1 score HAM 0.9859719438877755
F1 score SPAM 0.9616438356164384
SVM_Light
Precision ham 98.99497487437185
Precision spam 95.92391304347827
Recall ham 98.5
Recall spam 97.2451790633609
F1 score HAM 0.9874686716791979
F1 score SPAM 0.9658002735978113
MegaM Light
Precision ham 98.94625922023182
Precision spam 96.08695652173913
Recall ham 93.89999999999999
Recall spam 60.88154269972452
F1 score HAM 0.9635710620831195
F1 score SPAM 0.7453625632377741

SENTIMENT
Naive Bayes
Precision pos 87.06896551724138
Precision neg 82.08955223880598
Recall pos 80.80000000000001
Recall neg 88.0
F1 score POS 0.8381742738589211
F1 score NEG 0.8494208494208494
SVM_Light
Precision pos 87.87528868360278
Precision neg 87.10407239819004
Recall pos 86.97142857142856
Recall neg 88.0
F1 score POS 0.87421022400919
F1 score NEG 0.8754974417282548
MegaM Light
Precision pos 75.34562211981567
Precision neg 74.94331065759637
Recall pos 74.74285714285715
Recall neg 75.54285714285714
F1 score POS 0.7504302925989673
F1 score NEG 0.7524188958451906


I chose a 10% of the spam training data for the purpose of testing. The following are the scores obtained:
Naive Bayes
Precision ham 97.61194029850746
Precision spam 94.6927374301676
Recall ham 98.1
Recall spam 93.38842975206612
F1 score HAM 0.9785536159600997
F1 score SPAM 0.9403606102635229
SVM_Light
Precision ham 94.4980694980695
Precision spam 93.57798165137615
Recall ham 97.89999999999999
Recall spam 84.29752066115702
F1 score HAM 0.9616895874263262
F1 score SPAM 0.8869565217391305
MegaM Light
Precision ham 98.34196891191709
Precision spam 95.6896551724138
Recall ham 94.89999999999999
Recall spam 61.15702479338842
F1 score HAM 0.9659033078880407
F1 score SPAM 0.746218487394958

There seems to be a slight decrease in the F-score of Naive Bayes classifier and the SVM_Light classifier.
But not very significant. The reason for decrease could be that some of the prominent features from the whole training
set are not present. However I was expecting a significant decrease in the F-score , but it could be because the training set chosen
resembled the dev set very closely.
On the contrary MegaM MaxEntropy classifier seems to have slightly better F-score, this is again strange to me.
But the only possible explanation is that the training set possibly captured the features present in the dev set closely.
