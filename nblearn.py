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
	model_file = open(sys.argv[2], 'w')
	
	class_vocab_map = {} #a dictionary to between class and the vocabulary
	
	words = []
	
	for line in training_file:	
		vocab = {} #a dictionary to store the word and corresponding counts
		words = re.split(r'\s+' , line.rstrip()) #split on spaces and remove new line character
		
		if words[0] not in class_vocab_map:
			class_vocab_map[words[0]] = vocab
		else:
			vocab = class_vocab_map[words[0]]
			
		for word in words[1:]:
			if word not in vocab:
				vocab[word] = 1
			else:
				vocab[word] = vocab[word] + 1
						
		
	log = ""		
	for key in class_vocab_map:
		print(key)
		log += '<' + key + '>' + '\n'
		vocabulary = class_vocab_map[key]
		print(vocabulary)
		for item in sorted(vocabulary.keys()):
			log += '<' + item + '>' + str(vocabulary[item]) + '<' + '/' + item + '>' + '\n'
		print(str(len(vocabulary)))
		log+= '</' + key + '>'+ '\n'	
		
	model_file.write(log)
	
	training_file.close()	
	model_file.close()
	return


#boilerplate for main
if __name__ == '__main__':
	main()
