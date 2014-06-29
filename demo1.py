import random

list1=["shitou",'jiandao','bu']
computer=random.choice(list1)
list2=[['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]


person=raw_input("please enter 'shitou','jiandao','bu':")

print computer
print "-"*40

if person in list1:
    if computer == person:
        print "ping ju ..."
    else:
        if [computer,person] in list2:
            print "shengli computer  !!!"
        else:
            print "shengli person  !!!"
