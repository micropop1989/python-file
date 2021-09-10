x= 15
y= 30
myList = [{'foo':9,'bar':12},{'moo':11,'doo':10},{'coo':8,'zoo':1}]
#======================================
def fun():
    str1 = "xyz"
    x = 20
    return str1,x;
#=====================================
def fun2():
    str2 = "xyz"
    x2 = 20
    return [str2,x2];
#=====================================
def fun3():
    d = {}
    d['str2'] = "xyz"
    d['x2'] = 20
    return d
#=======================================
def cal(x,y):
    z= x + y
    return z;
#======================================
def list2(myList):
    print(myList)
    print(myList[1]['doo'])
#=======================================
str1, x1 = fun()
result = fun()
list1 = fun2()
c = fun()
d = fun3()
print('type for fun():',type(c))
print(str1)
print(x1)
print(list1)
print('dict x2=',d.get('x2'))
print('type for fun2:',type(list1))
print(d)
print('type for fun3:',type(d))
print('the value for fun x:',result[0])
z1 = cal(x,y)
print('z=',z1)
list2(myList)


