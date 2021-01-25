from nltk.corpus import words
import inspect

file = open('words.txt','r+')

english = [w.lower() for w in words.words()]
temp = 'a'



for each in english:
    if temp[0]!=each[0]:
        file.write('\n')
    file.write(each+'$')
    temp = each



file.close()
