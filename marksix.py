''' MARKSIX SIMULATOR '''

import random

win = False
n = 0

def randomno(no):
    myno = []
    while len(myno) != no:
        fulllist = list(range(1,49))
        x = random.choice(fulllist)
        myno.append(x)
        fulllist.remove(x)   
    return myno

while win == False:
    mine = randomno(6)
    jc = randomno(7)
    for i in range(0,5):
        if mine(i) in 
    if mine in (jc):
        win = True
        print ("Got it! It took %i attempts" %n)
    else:
        n += 1
        print ('now %i attempt' %n)


        
    
