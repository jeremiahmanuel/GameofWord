from nltk.corpus import words
import enchant

file = open('words.txt','r+')

#english = [w.lower() for w in words.words()]
temp = ' '
d = enchant.Dict('en_US')
letters = list(input('enter the letters: ').lower())
wlength = 0
wlength = input('enter the lenght(optional): ')
if wlength is None or len(wlength) == 0 :
    wlength = 0
else:
    wlength = int(wlength)

res = []

flag = True

for line in file:
    firstWord = line.split('$',1)[0]
    if len(firstWord) == 0 or firstWord is None :
        print('empty string')
        continue
    if firstWord[0] in set(letters):
        for word in line.split('$'):
            if len(word)<3 or word in res :
                continue
            for i in set(list(word)):
                if i not in set(letters):
                    flag = False
                    break
            if flag and d.check(word) :
                res.append(word)
            flag = True
    else:
        continue

for i in res :
    if wlength > 0 :
        if len(i) == wlength :
            print(i)
    else :
        print(i)

file.close()
