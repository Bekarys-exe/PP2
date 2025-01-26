#What will be the result of the following syntax:
print(5 > 3)

#True

print(10 > 9)

#True

print(10 == 9)

#False

print(bool("abc"))

#True

print(bool(0))

#False

#What will be the result of the following syntax:
x = 5
x += 3
print(x)

#8

#Multiply 10 with 5, and print the result.

print(10*5)

#Divide 10 by 2, and print the result.

print(10/2)

#Use the correct membership operator to check if "apple" is present in the fruits object.

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Use the correct comparison operator to check if 5 is not equal to 10.

if 5!=10:
  print("5 and 10 is not equal")

#Use the correct logical operator to check if at least one of two statements is True.

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])

#banana

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])

#banana

'''
True or False.
List items cannot be removed after the list has been created.
False
'''

#Select the correct function for returning the number of items in a list:
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])

#cherry

#Print the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])

#['banana', 'cherry', 'orange']

#Use a range of indexes to print the third, fourth, and fifth item in the list.

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

#banana

#Change the value from "apple" to "kiwi", in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

#mango

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])

#apple

#Use the append method to add "orange" to the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Use the insert method to add "lemon" as the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#Select the missing parts to add the elements of tropical to fruits:

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

'''
What is a List method for removing list items?

pop()
'''

#Use the remove method to remove "banana" from the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)

#['apple', 'cherry']

#Select the correct function to remove all items from a list:

fruits = ['apple', 'banana', 'cherry']
fruits.clear()

#What is a correct syntax for looping through the items of a list?

for x in ['apple', 'banana', 'cherry']:
  print(x)

#Insert the missing part of the while loop below to loop through the items of a list.

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

#What is a correct syntax for looping through the items of a list?

[print(x) for x in ['apple', 'banana', 'cherry']]

#Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
#What will be the value of newlist?

['banana']

#Fill in the missing parts to complete the list comprehension:

fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

#Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
#What will be the value of newlist?

#['apple', 'apple', 'apple']

'''
What is a correct syntax for sorting a list?

mylist.sort()
'''

'''
What is a correct syntax for reversing the current order of a list?

mylist.reverse()
'''

'''
What is a correct syntax for sorting a list descending?

mylist.sort(reverse = True)
'''

'''

What is a correct syntax for making a copy of a list?

list2 = list1.copy()
'''

'''
What is a correct syntax for making a copy of a list?

list2 = list(list1)
'''

'''
What is a correct syntax for making a copy of a list?

list2 = list1[:]
'''

'''

What is a correct syntax for joining list1 and list2 into list3?

list3 = list1 + list2
'''

'''
What is a correct syntax for adding elements from list2 into list1?

list1.extend(list2)
'''

#Consider the following code:
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
#What will be the value of list1?

#['a', 'b', 'c', 1, 2, 3]

#Which one of these is a tuple?

thistuple = ('apple', 'banana', 'cherry')

#Use the correct syntax to print the number of items in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(len(fruits))

'''
True or False.
Tuple items cannot be removed after the tuple has been created.

True
'''

'''
You can access tuple items by referring to the index number, but what is the index number of the first item?

0
'''

#Use the correct syntax to print the first item in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Use negative indexing to print the last item in the tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the tuple.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

'''
You cannot change the items of a tuple, but there are workarounds. Which of the following suggestion will work?

Convert tuple into a list, change item, convert back into a tuple.
'''

'''
Which is a correct syntax to delete a tuple?

del mytuple
'''

'''
True or False. You are allowed to add a tuple to an existing tuple.

True
'''

#Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
#What will be the value of y?

#banana

#Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#What will be the value of y?

#['banana', 'cherry']

#Consider the following code:
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#What will be the value of y?

#['banana', 'cherry']

#What is a correct syntax for looping through the items of a tuple?

for x in ('apple', 'banana', 'cherry'):
  print(x)

#Insert the missing part of the while loop below to loop through the items of a tuple.

mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1

#Insert the missing part of the for loop below to loop through the items of a tuple by using the range function to loop through the tuple's index numbers.

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#What is a correct syntax for joining tuple1 and tuple2 into tuple3?
tuple1 = (1 , 2 , 3)
tuple2 = ( 4 , 5 , 6)
tuple3 = tuple1 + tuple2

#What is a legal way to turn this tuple: (1,2,3) into this tuple:(1,2,3,1,2,3)?

tuple1 = (1,2,3)
tuple1 = tuple1 * 2

#Consider the following code:
tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
#What will be the value of tuple3?

#(1, 2, 3, 'a', 'b', 'c')

#Which one of these is a set?

myset = {'apple', 'banana', 'cherry'}

'''
True or False.
Set items cannot be removed after the set has been created.

False
'''

'''
True or False.
A set cannot have two items with the same value.

True
'''

#Select the correct function for returning the number of items in a set:

fruits = {'apple', 'banana', 'cherry'}
print(len(fruits))

'''
True or False. You can access set items by referring to the index.

False
'''

#Check if "apple" is present in the fruits set.

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Consider the following code:
thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)
#What will be the printed result?

#False

'''
What is a correct syntax for adding items to a set?

add()
'''

#Use the add method to add "orange" to the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Use the correct method to add multiple items (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

'''
What is a correct syntax for removing an item from a set?

remove()
'''

#Use the remove method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Use the discard method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Select the correct function to remove all items from a set:

fruits = {'apple', 'banana', 'cherry'}
fruits.clear()

#What is a correct syntax for looping through the items of a set?

for x in {'apple', 'banana', 'cherry'}:
  print(x)

#Insert the missing part of the for loop below to loop through the items of a set.

myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)

'''
True or False. Sets are unordered, so when you loop through the items, the order will be totally random.

True
'''

'''
What is a correct syntax for joining set1 and set2 into set3?

set3 = set1.union(set2)
'''

'''
What is a correct syntax for joining multiple sets into one new set called set5?

set5 = set1 | set2 | set3 | set4
'''

'''
There are many ways to join sets in Python. Which one of the following methods keeps ONLY the duplicates?

intersection()
'''

#Which one of these is a dictionary?

x = {'type' : 'fruit', 'name' : 'banana'}

'''
True or False.
Dictionary items cannot be removed after the dictionary has been created.

False
'''

'''
True or False.
A dictionary cannot have two keys with the same name.

True
'''

#Select the correct function to print the number of key/value pairs in the dictionary:

x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

'''
True or False. You can access item values by referring to the key name.

True
'''

#Use the get method to print the value of the "model" key of the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Consider the following code:
x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])
#What will be the printed result?

#fruit

#Consider the following code:
x = {'type' : 'fruit', 'name' : 'banana'}
#What is a correct syntax for changing the type from fruit to berry?

x['type'] = 'berry'

#Change the "year" value from 1964 to 2020.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Consider the following code:
x = {'type' : 'fruit', 'name' : 'banana'}
#What is a correct syntax for changing the name from banana to apple?

x.update({'name': 'apple'})

'''
Which one of these dictionary methods can be used to add items to a dictionary?

update()
'''

#Add the key/value pair "color" : "red" to the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Insert the missing part to add an item to the dictionary.

x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' : 'green'})

'''
What is a dictionary method for removing an item from a dictionary?

pop()
'''

#Use the pop method to remove "model" from the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Use the clear method to empty the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#Insert a correct syntax for removing the 'color' item of the dictionary:

myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar['color']


#What is a correct syntax for looping through the values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}

for y in x.values():
  print(y)

#What is a correct syntax for looping through the keys AND values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}

for y, z in x.items():
  print(y, z)

#Insert the missing part of the for loop below to loop through the items of a set.

myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)

#What is a correct syntax for looping through the keys of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}

for y in x.keys():
  print(y)

#What is a correct syntax for making a copy of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}

y = x.copy()

#One of these codes is NOT a correct way of making a copy of a dictionary named x, which one:

y = x.duplicate()

'''
True or False. Copied dictionaries will not be able to change its item values.

False
'''

#Consider this syntax:
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
#what will be a correct syntax for printing the name 'May'?

print(customers['c2']['name'])

'''
Insert the missing part to loop through the keys and values of all nested dictionaries:

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])
'''

'''
True or False. A dictionary can only have one level of nested dictionaries.

False
'''

'''
What will be the result of the following code:
x = 5
y = 8
if x > y:
  print('Hello')
else:
  print('Welcome')

Welcome
'''

'''
Print "Hello World" if a is greater than b.

a = 50
b = 10
if a > b:
  print("Hello World")
'''

'''
Print "Hello World" if a is not equal to b.

a = 50
b = 10
if a != b:
  print("Hello World")
'''

'''
Print "Yes" if a is equal to b, otherwise print "No".

a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
'''

'''
Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
'''

'''
Print "Hello" if a is equal to b, and c is equal to d.

if a == b and c == d:
  print("Hello")
'''

'''
Print "Hello" if a is equal to b, or if c is equal to d.

if a == b 
or
 c == d:
  print("Hello")
'''

'''
Complete the code block, print "YES" if 5 is larger than 2.

Hint: remember the indentation.

if 5 > 2:
    print("YES")
'''

'''
Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").

a = 2
b = 5
print("YES") if a == b else print("NO")
'''

'''
Which statement is a correct syntax to break out of a loop?

break
'''

'''
Print i as long as i is less than 6.

i = 1
while i < 6:
  print(i)
  i += 1
'''

'''
Stop the loop if i is 3.

i = 1
while i < 6:
  if i == 3:
    break
  i += 1
'''

'''
In the loop, when i is 3, jump directly to the next iteration.

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''

'''
Print a message once the condition is false.

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''

'''
What will be the result of the following code:
for x in range(3):
  print(x)

0
1
2
'''

'''
Loop through the items in the fruits list.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''

'''
In the loop, when the item value is "banana", jump directly to the next item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''

'''
Use the range function to loop through a code set 6 times.

for x in range(6):
  print(x)
'''

'''
Exit the loop when x is "banana".

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
'''

a = input()