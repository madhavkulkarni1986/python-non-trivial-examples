import sys
import re
'''
Script takes file name as command line argument and does a word count of the the words in the file. 
It only prints the word that appears the most in the below format:

Output: Word: <word> -> Occurance: <no of occurance>
        Ex: Word: Python -> Occurance: 4

'''

## Check if file name is given as agument. Exit if file is not provided
if(len(sys.argv) != 2):
   print("Insufficient number of arguments")
   print("[Usage] basic_word_count.py <filename>")
   sys.exit(1)

## Assign file name to a variable
filename = sys.argv[1]

## Initialize some dictionary for operation
words = dict()
new_words=dict()

## Catch IOError to make sure the file provided as argument exist
try:
   with open(filename) as filee:
      ## Reach each word from the file and assign it to the dictionary(words)      
      for word in filee.read().split():
         if(word not in words):
            words[word] = 1
         else:
            words[word] += 1
except(IOError):
   print "The file {} does not exist".format(filename)
   sys.exit(1)

## Create a dictionary of array with the keys being the count of a word and the array being the words itself
## Example: If each of the words 'mickey' 'tommy' 'jerry' and 'minney' occur 3 times in the file, the dictionary will be
##          new_words[3] = ['mickey','tommy', 'jerry','minney']
for i in words:
   if words[i] not in new_words:
      new_words[words[i]] = []
      new_words[words[i]].append(i)
   else:
      new_words[words[i]].append(i)

## Create a new array with the keys of new_words
keylist = new_words.keys()

## Find the maximum of the keys
maxi=max(keylist)

## Print the words with the maximum count
for val in new_words[maxi]:
   print("Word: {} -> Occurance: {}".format(val,maxi))