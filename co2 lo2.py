# python tuple:
  # tuple is a collection , which is ordered and unchangeable.
  # tuple are written without roundbrackets.
    # create a tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# output: ('apple', 'banana', 'cherry')
thistuple = ("apple","cherry","banana")
print(thistuple)
# output: ('apple', 'cherry', 'banana')


# INDEXING IN TUPLE:
  # INDEXING  is same as list and array has.starting with zero and last index is n-1.
  # n is the length of the list.
  # it also has negative indexing.
  #last element -1 to end.



  # ACCESS TUPLE ITEMS:
     # BY referring to the index number inside square brackets , can access a tuple.
     # print the second item of the tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # output : banana
print(thistuple[-1]) # output: cherry.

digital = ("apple", "banana", "cherry")
print(digital[1]) # output : banana
print(digital[-1]) # output: cherry.


# CONVERTING TUPLE TO LIST:
  # tuple value once created then it is unchangeable.
  # you can convert tuple to list, change the list and convert the list back into a tuple.
  # Eg:
     # convert the tuple into  a list to be able to change it:
x = ("apple", "banana","cherry")
y = list(x)
y[0] = "kiwi"
x = tuple(y)
print(x) # output: ('kiwi', 'banana', 'cherry')


# ITERATING OVER TUPLE:
   # iterate through the items and print the values:
   # works same as list.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)  # output: apple
                      # banana
                       #cherry


  # CHECK IF THE ITEM EXISTS:
    # to check presence of a item in tuple  use the "in" keyword.
    # check if apple is present in the tuple:
thistuple = ("apple","banana", "orange")
if "apple" in thistuple:
    print("yes, 'apple' is in the fruits tuple")
#
thistuple = ("apple", "banana", "orange")
if "Dj" in thistuple:
    print("yes, 'apple' is in the fruits tuple")
else:
    print("no babe!!!")
    # output: no babe!!!



# TUPLE LENGTH:
   # by using len() , you can find no. of items.
   # Eg:
        # print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # output: 3


# JOIN TWO TUPLES:
  # join two or more tuple  use + operators
  # Eg:
     # join two tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3) # output: ('a', 'b', 'c', 1, 2, 3)



# tuple methods:
   # count() , returns the number of times a specified value occurs in a tuple
   # index(), searches the tuple for a specified value and returns the position of where it was found.



# PYTHON SETS:
 # set is collection , which is unordered and unindexed.
 # sets are written in curly brackets.
 # create a set:
thisset = {"apple", "djdj", "cherry"}
print(thisset) # output: {'apple', 'cherry', 'djdj'}


  # access item:
    # set items cannot access by an index or a key.
    # can accessed by a  'for' loop, or by asking if a specified value is present in a set, by using the 'in' keyword.
    # Eg:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)  # output: cherry
                        # apple
                         #  banana

# ADD ITEMS:
  # to add item to set is by using add() method, for only one item.
  # to add more than one item to a set use the update() method.
   # Eg:
    # add a item to set by using add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # output:{'apple', 'cherry', 'banana', 'orange'}


# to add multiple items:update() method:
thisset = {"apple ", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset) # {'grapes', 'mango', 'apple ', 'cherry', 'banana', 'orange'}




# length of a set:
  # to determine how many items a set has, use the len() method.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # output: 3

# remove item.
  # use remove(), or discard()
  # remove banana by using the remove() method:
thisset = {"apple", "banana","cherry"}
thisset.remove("banana")
print(thisset) # output: {'apple', 'cherry'}, if the item to remove not exist , remove() will generate an error.
               # discard and remove takes only one argument at one time.
thisset = {"apple", "banana","cherry"}
thisset.discard("banana")
print(thisset) # output: {'apple', 'cherry'}, if the item to remove not exist , discard() will not generate an error.


# we can also use the pop method  to remove an item but this will remove last item.
 # remove the last item by using the pop() method:

thisset = {"apple", "banana","cherry"}
thisset.pop()
print(thisset)
# output: banana, apple
# sets are unordered , so you will not know what item , gets removed.



#JOINING OF TWO SETS:
   # by union(), it returns a new set containing all items from both sets .
   # by update(), this inserts all the itemss from one set into another:
      # joining by union():
set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)  # output: {1, 2, 3, 'b', 'c', 'a'}
    # joining by update():
set1 = {"a", "b", "c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)  # output: {'b', 1, 2, 'a', 3, 'c'}
# results for sets changes every time you execute it.
# union() and update() both will exclude any duplicate items.


# PYTHON SET OPERATIONS:
  # union, intersection, differece and symmetric difference
    # operands used for different operations:
       # | for union
       # & for intersection
       # - for difference
       # ^ for symmetric difference
   # eg:

A = {0,2,4,6,8}
B = {1,2,3,4,5}
# union
print("union:", A|B)  # output: union: {0, 1, 2, 3, 4, 5, 6, 8}
# intersection:
print("intersection", A & B) # output: intersection {2, 4}
# difference
print("Difference: ",A-B) # output: Difference:  {0, 8, 6}
print("Difference: ",B-A) # output: Difference: {1, 3, 5}
#symmetric difference:
print("symmetric difference:", A^B) # output: {0,1,3,5,6,8}


# PYTHON DICTIONARY:
  # dictionary is a collection, which is unordered, changeable and indexed.
  # dictionary written with curly brackets .
  # dictionary has a key and a value pair.
  # eg:
    # create and print a dictionary.
thisdict = {
       "brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964
              }
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

   # Add item to dictionary:
      # dictionary name with  new index key and assigned value .
thisdict["color"] = "red"
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# REMOVE ITEM:
   # remove by pop() method:

thisdict = {
       "brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964
              }

thisdict.pop("model")
print(thisdict) # output: {'brand': 'Ford', 'year': 1964}

   # remove by using del keyword:
     # removes the item with the specific key name.
thisdict = {
       "brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964
              }
del thisdict["model"]
print(thisdict) # output: {'brand': 'Ford', 'year': 1964}
del thisdict["brand"]
print(thisdict) # output: {'year': 1964}
# del keyword also used to delete complete dictionary.
'''
thisdict = {
       "brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964
              }
del thisdict
print(thisdict) # output : shows an error because thisdict does not exist.
'''


 # Access an item:
   # you can access item by referring to its keyname , inside square brackets:
    # eg:
      # get the value of the "model" key.
thisdict = {"brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964}
x = thisdict["model"]
print(x) # output : Mustang

x = thisdict["year"]
print(x) # output: 1964

  # by get()  method gives same result :
thisdict = {"brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964}
x = thisdict.get("model")
print(x) # output : Mustang

     # CHANGING THE ITEM VALUES:
        # change item value by referrig its keyname.

thisdict = {"brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964}
thisdict["year"] = 2000
print(thisdict) # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2000}


  # ITERATION OVER DICTIONARY:
     # can loop through a dictionary by using a for loop.
     # return value is keys of dictionary but , by methods value also can be return.
     # eg:
       # print all the names of dictionary one by one
thisdict = {"brand" : "Ford",
     "model" : "Mustang",
    "year" : 1964}
for x in thisdict:
    print(x)
# output:
'''
brand
model
year
'''

 # print all the values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
    #output:
    '''
    Ford
    Mustang
    1964'''

    # to print all the value you can also use values() method.
for x in thisdict.values():
    print(x)
# output:
'''
Ford
Mustang
1964
'''

# loop through both keys and values by using items() method:
for x,y in thisdict.items():
    print(x,y)

# output: #brand Ford
# model Mustang
# year 1964


# CHECK IF KEY EXISTS:
  # to check specified key is present use in keyword:
   # eg:
      # check if "model" is present in the dictionray:

thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964}
if "model" in thisdict:
    print("yes, 'model' is one of the keys")
    # output: yes, 'model' is one of the keys


    # LENGTH OF DICTIONARY:
      # USE LEN() FUNCTION.
      # EG:print the number of items in the dictionary:

thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964}
print(len(thisdict)) # output: 3


    # COPY DICTIONARY:

  # you cannot copy a dictionary by dict2 = dict1
   # because dict2 will only be refrence to dict1 and changes made in dict1 will automatically also be made
   # in dict2
   # to copy use copy() method.
   # Eg: make a copy of a dictionary with the copy() method:
thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964}
mydict = thisdict.copy()
print(mydict)  # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
  # another way to copy is to use a built-in function dict()
  # eg: make a copy of dictionary with the dict() function:
thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964}
mydict = dict(thisdict)
print(mydict)  # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}









