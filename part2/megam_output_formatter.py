

import re
import sys

def main():
    if len(sys.argv) < 4:
        print("usage: python3 output_formatter.py --svm/megam --spam/sent filename output_file")
        return
    
    input_file = open(sys.argv[3],'r+')
    output_file = open(sys.argv[4],'w+')
    result = 0.0
    if sys.argv[1] == '--svm':
        
        if sys.argv[2] == '--spam':
            for line in input_file:
                result = float(line.rstrip())
                print(result)
                if result > 0.0:
                    output_file.write('HAM\n')
                else:
                    output_file.write('SPAM\n')
        else:
            for line in input_file:
                result = float(line.rstrip())
                print(result)
                if result > 0.0:
                    output_file.write('POS\n')
                else:
                    output_file.write('NEG\n')
                    
    elif sys.argv[1] == '--megam':
        if sys.argv[2] == '--spam':
            for line in input_file:
                result = re.split(r'\s',line.rstrip())[0]
                print(result)
                if result == '1':
                    output_file.write('HAM\n')
                else:
                    output_file.write('SPAM\n')
        else:
            for line in input_file:
                result = re.split(r'\s',line.rstrip())[0]
                print(result)
                if result == '1':
                    output_file.write('POS\n')
                else:
                    output_file.write('NEG\n')


#boilerplate
if __name__ == '__main__':
    main()
