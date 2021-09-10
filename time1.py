from time import time
from random import randint
#time()
#print("time %-5.5ss" %time())
#x = randint(0,9)
#print('temp %s' %x)
#for _ in range(5):
 #   value = randint(0, 10)
  #  if value < 5:
   #     print('small')
    #else:
     #   print('big')
    #print(value)
guass = randint(1,99)
minimun = 0
maximun = 99
t1 = 0
t2 = 5
print('guass a number, you got 5 times chance!!')
print('----------------------------------------')
print('Enter the chance')
t2 = int(input())
while True:
    print('enter a value')
    number1 = int(input())
    t1 +=1
    
    if number1 < guass:
        
        if number1 > minimun and number1 < maximun:
            minimun = number1
            
            #print('small')
            print('range: ' ,minimun,maximun)
            
            
        else:
            print('invalid')
        if t1 == t2:
                print('Game Over!!!')
                
                break
    elif number1 > guass:
        if number1 > minimun and number1 < maximun:
            maximun = number1
            
            #print('big')
            print('range: ' ,minimun,maximun)
            
            
        else:
            print('invalid')
        if t1 == t2:
                print('Game Over!!!')
                
                break
    elif number1 == guass:
        
        print('YOU WIN!!!')
        
        break
    print('%s times' %t1)
print('correct:',guass)
