'''
Normally, a (pseudo-)random number generator is a deterministic algorithm that given an initial number (called seed), generates a sequence of numbers that adequately satisfies statistical randomness tests. Since the algorithm is deterministic, the algorithm will always generate the exact same sequence of numbers if it's initialized with the same seed. That's why system time (something that changes all the time) is usually used as the seed for random number generators.

The seed for each PRNG will be the result of this.

A single tick represents one hundred nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond, or 10 million ticks in a second. This will allow enough spread between occaisonally retreived ticks, where we can assume reasonable pseudo-unpredictabililty. This serves as a simplistic and constantly changing control mechanism for being able to seed PRNGs and test experimental outcomes. While not the most cryptographically strong, we needed a way to have some controlled aspect of seed generation to feed into generators of varying cryptographic complexity (to have some baseline of comparison).

Note that t is an optional parameter if needed. Since the calls are genralized in DataBroker, parameters have to be the same.

'''

from datetime import *
from time import sleep

def ticks(t):
    t = int( str( int( (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 10000000))[-6:])
    if(t==0):
        t = ticks()
    return t
        
    #return (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()


def ticks_LF(t):
    seed = int(str( int( (datetime.utcnow() - datetime(1, 1, 1)).total_seconds() * 10000000 ))[-10:])
    
    flag = False
    for i in range(len(str(seed))):
        if(int(str(seed)[i]) % 2 == 0):
            flag = False
        else: # if digit is odd, we can break out of loop
            flag = True
            break;

    if(flag):
        return seed
    else:
        seed = ticks_LF(t)
        
    return seed

    
    
def ticks_WH(t):
    lst = []
    for i in range(3):
        lst.append(ticks(t))
        #time delay
        #print(lst[i], end = ' ')
        #print(lst[i],end = ' ')
        sleep(1/lst[i])
    return lst

