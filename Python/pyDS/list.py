#built in function or constructor
empty_list=list()#this is an empty list , no item in the list
print(len(empty_list))#0

#using square bracket
empty_list=[]#this is an empty list , no item in the list
print(len(empty_list))#0

"""
fruits=['banana','orange','mango','lemon']
vegetables=['Tomato','Potato','Cabbage', 'Onion','Carrot']
animal_products=['milk','meat','butter','yoghurt']
web_techs=['HTML','CSS','JS','React','Redux','Node','MongoDB']
countries=['Finland','Estonia','Denmark','Sweden','Norway']
print(fruits)
print(len(fruits))
print(vegetables)
print(len(vegetables))
"""

"""
fruits=['banana', 'orange', 'mango', 'lemon']                     # list of fruits
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

vegetables=['Tomato','Potato','Cabbage', 'Onion','Carrot']
all_fruits=fruits[0:4]
print(fruits[0:3])
print(vegetables[::2]) #slicing
print(vegetables[1:])
print(fruits[:3])
"""
"""

# list of fruits
fruits=['banana', 'orange', 'mango', 'lemon']
print(fruits)
#adding the item
fruits.append('apple')
print(fruits)
fruits.append('lemon')
print(fruits)
print(len(fruits))
print(fruits[len(fruits)-1])
print(fruits[-1])"""

# list of fruits
fruits=['banana', 'orange', 'mango', 'lemon']
print(fruits)
#adding the item
fruits.append('apple') #adding to the last value in the List
print(fruits)  #printing the current list values
fruits.append('lemon') #adding to the last value in the List
print(fruits)
print(len(fruits)) #finding the length of the list(fruits)
print(fruits[len(fruits)-1])#print the last value
print(fruits[-1]) #print the last value
fruits.insert(2, 'xyz') #insert method used to insert particular place
print(fruits)
fruits.remove('xyz') #remove the item in the list
print(fruits) #it shows the list values
fruits.pop() # it remove the last item in the list
print(fruits)
fruits.pop(2) #pop pass the index place to remove
print(fruits)
del fruits[0]  #delete the particular index value
print(fruits)
fruitscopy=fruits.copy()
print(fruitscopy)
fruits.clear() # clearning the all the elements in the list
print(fruits)
fruits=['banana', 'orange', 'mango', 'lemon','orange']
print("count value",fruits.count('orange'))

fruits1=['a','b','c']
joinfruit=fruitscopy+fruits1
fruits2=['d','e','f']
fruits2.extend(fruits1)
print("Fruits2 extend:",fruits2)
print(fruits2.index('f') )
fruits2.reverse()
print(fruits2)
fruits2.sort()
print(fruits2)
fruits2.sort(reverse=True)
print(fruits2)
numlist=[100,290,478,345,567,1000]
print("Maximum value:" ,max(numlist))
print("Minimum value:",min(numlist))
print("Sum value:",sum(numlist))
print("Length value:",len(numlist))
print("Average value:",sum(numlist)/len(numlist))
print("Numlis value using iterator:")
for i in numlist:   #Iterator using the for loop.
    print(i,end=' ')
print('\n')
print("Current fruit list",fruitscopy)
myfruits=', '.join(fruitscopy) #join method is used go generate the normal values
print(myfruits)  #join method is the string datatype method
del fruits  # delete the entire list
print(fruits)

del fruits  # delete the entire list
print(fruits)
