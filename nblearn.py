#Naive Bayes Classifier - Author Majisha
#this code is to learn from the training file(input argument)
#and develop a learning model that will be saved in a model 
#file (input argument) 
import sys
import re
def main():
	
	if len(sys.argv) < 2:
		print("Invalid syntax")
		exit(0)
	
	#open training file
	training_file = open(sys.argv[1], 'r')
	class_set = set() #all possible classifications HAM or SPAM etc
	class_vocab_map = {}
	class_list = []
	
	words = []
	
	for line in training_file:	
		vocab = {} #a dictionary to store the word and corresponding counts
		words = re.split(r'\s+' , line.rstrip())
		
		for word in words[1:]:
			if word not in vocab:
				vocab[word] = 1
			else:
				vocab[word] = vocab[word] + 1
						
		if words[0] not in class_vocab_map:
			class_vocab_map[words[0]] = vocab
		else:
			class_vocab_map[words[0]].update(vocab)
	print(class_vocab_map)
		
	return


#boilerplate for main
if __name__ == '__main__':
	main()
