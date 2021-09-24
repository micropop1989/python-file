for x in range(2, 6):
  print(x)
  
#==========================
for y in range(2, 30, 3):
  print(y)
  
#===============================
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry", "grape"]

for a in adj:
  for b in fruits:
    print(a,b)
 
 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))