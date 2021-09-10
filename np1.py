fruits = ['apple','lemon','orange','grape','lemon']
words={'apple':'red','lemon':'red','orange':'orange','payaya':'yellow'}
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Male'}}


fruits.append('blueberry') #add list item
key = 'lemon'
words['grape'] = 'barnana' #add dict item

####################### check key in dict
if words.get(key) is not None:
    print(f"Yes, key: '{key}' exists")
else:
    print(f"No, key: '{key}' Not exists")
##########################
#print(words.values('apple'))
#hello()

#=========================================
#print all list & dict function
def print_list():
    print(fruits[-1]) #print last item
    print(fruits[2]) #print 3nd items
    print(fruits)
    print(fruits.index('lemon'))
    print(len(fruits))
    print('apple' in fruits)
    print(words['apple'])
    print(words)
    print(words.keys())
    print(words.values())
#===========================================
#print fruits list function
def fruits_list(food):
    print('x list values')
    for x in food:
        print(x)
    print('y list values')
    for y in sorted(set(food)):
        print(y)
#==============================================
#print word list function
def word_dict(w1):
    w1.pop('lemon') #remove item
    w1.popitem() #remove item
    w1_items = w1.items()
    w1_values = w1.values()
    print('x dict')
    for x in w1:
        print(x) #Print key
    for y in w1_items:
        print(y) #print item
    for z in w1_values:
        print(z) #print vlaue

    for key, value in w1.items():
        print(key, ':', value) #print key value pair
#========================================================
#print people list function
def people_dict(pp):
    for p_id, p_info in pp.items():
        print("\nPerson ID:", p_id)
        for key in p_info:
            if key == 'name':
                print('Name' + ':', p_info[key])
            elif key == 'sex':
                print('SEX' + ':', p_info[key])
#========================================================
#clear list
def fruits_clear(food):
    food.clear()
    print(food)
#=========================================================
                
#call function
print_list()
fruits_list(fruits)
word_dict(words)
people_dict(people)
fruits_clear(fruits)
x= 2
print(pow(x,3))
