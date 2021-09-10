#IPO - Input, Process, Output
'''
hello
'''
#for i in range(10):
print("tem")
temp2 =25
val2 = input("你好，请输入你要的东西")
if val2[-1] in ['C', 'c']:
    f=1.8 * float(val2[0:-1]) +32
    print("we %.2fF"%f)
elif val2[-1] in ['F', 'f']:
    c= (float(val2[0:-1]) - 32) / 1.8
    print("we %.2fC"%c)
else:
    print("error")


'''
and as assert break class continue def del elif else except False finally for from
global if import in is lambda None nonlocal not or pass raise return True try while
with yield
'''
num1 = input("first")
num2 = input("Second")
avg_num = (float(num1) + float(num2)) /2
print("average %f" %avg_num)
