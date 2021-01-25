from nltk import everygrams as eg
import enchant

d = enchant.Dict('en_US')

letters = list(input('enter the letters  '))
res = [''.join(ww) for ww in eg(letters) if d.check(''.join(ww)) and len(ww)>2]
for i in res:
    print(i)
