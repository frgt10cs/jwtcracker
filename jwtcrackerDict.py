#!/usr/bin/python3

import sys
import hmac
import hashlib
import base64

token = sys.argv[1]
filename = sys.argv[2]
words = open(filename,encoding='utf-8').read().split("\n")
wordsLength = len(words)
print("words count: ",wordsLength)
splitted = token.split('.')
tokenHeader = splitted[0]
tokenPayloads = splitted[1]
tokenSignature = splitted[2]

def printProgressBar (iteration, total= wordsLength-1, prefix = 'Checking', suffix = 'Complete', decimals = 1, length = 50, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    styling = '%s |%s| %s%% %s' % (prefix, fill, percent, suffix)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s' % styling.replace(fill, bar), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

printProgressBar(0)
i=0
for word in words:
    wordBytes= word.encode("utf-8")    
    dig = hmac.new(wordBytes, msg=(tokenHeader+"."+tokenPayloads).encode(), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(dig).decode().replace("=","").replace("+","-")
    printProgressBar(i,wordsLength-1)    
    i+=1    
    if(signature==tokenSignature):
        printProgressBar(wordsLength-1)  
        print("Secret is: "+word)
        exit()  
print("Secret is not in dictionary")