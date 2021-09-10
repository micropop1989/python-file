import turtle #乌龟画图

def drawSnake(rad, angle, len, neckrad): #def - function
    for i in range(len) :
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad) # turtle forward()
    turtle.circle(neckrad+1, 180)
    #turtle.circle(-neckrad+1, 180)
    turtle.fd(rad*1/2)
    turtle.fd(150)

def main():
    turtle.setup(1300, 800, 0, 0)  #(w,h,x,y)
    pythonsize = 30 #pen size
    turtle.pensize(pythonsize)
    turtle.pencolor("red") #"#3B9909"
    turtle.seth(-40) #负40度
    drawSnake(40,80,5,pythonsize/2)
    #drawSnake(10,120,2,pythonsize/2)
    turtle.circle(-90, 180)

main()

#

#math
#random
#turtle
