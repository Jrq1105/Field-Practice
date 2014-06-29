#coding:cp936
import random

color=['fangpian','honghtao','heitao','meihua']
number=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']

deck=[]

for c in color:
	for n in  number:
		deck.append('%s of %s'%(c,n))

for x in range(3):
    random.shuffle(deck)


while deck:
    raw_input(deck.pop())
    
