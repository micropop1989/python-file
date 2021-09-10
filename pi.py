from random import random
from math import sqrt
from time import time
DARTS = 1200
hits = 0
time()
#t1 = time.ctime()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    #print('%s' %x)
    #print('%s' %y)
    #print('%s' %dist)
    if dist <= 1.0:
        hits = hits +1

pi = 4 * (hits/DARTS)
print("%s" %pi)
print("time %-5.5ss" %time())
#print(t1)

