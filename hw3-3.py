eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('Enter 1, in english, or 0, if in russian: ')))
word = input('Enter word: ').upper()
if N == 1:
	print('For this word you get', sum([k for i in word for k, v in eng.items() if i in v]), 'score')
elif N == 0:
	print('For this word you get', sum([k for i in word for k, v in rus.items() if i in v]), 'score')
else:
    print('You are cheating!')

 