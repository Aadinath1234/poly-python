# conditional statements:
 # equal  ==
 # not equal !=
 # less than <
 # less than or equal to <=
 # greater than >
 # greater than or equal to >=



 # if statement:
a = 10
b = 20
if b>a:
    print("b is greater than a") # the output is b is greater than a.

# Elif statement:
   # if previous is not true then try next/this condition.
a = 10
b = 20
if a>b:
    print("b is greater")
elif a < b:
    print("a is lesser than b") # the output is a is lesser than b.

# else statement:
a = 10
b = 20
if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print(" a is greater than b") # output: b is greater than a

  # when you have only one statement to execute, you can put it on the same line as the if statement.
a = 2
b = 1
if a > b: print(" a is greater than b")  # output : a is greater than b

# another example:
a = 2
b = 3
print("A") if a > b  else print("B")


'''
a = 2
b = 3
print("A") if a > b  elif:print("dj") else print("B")
# this will get an error.

'''
# another example:
a = 10
b = 10
print("A") if a > b else print("=") if a == b else print("B") # output : =


# logical 'and' and 'or' operator to combine more than one conditional statement:
    # test if a is greater than b, AND if c is greater than a:
a = 3
b = 2
c = 4
if a > b and c >a:
    print("both conditions are TRUE")  # both conditions are true.

  # NESTED IF STATEMENTS:

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
    # output : above ten, and also above 20!.


    # if statement cannot be empty . to not to get error , then use pass statement.

a = 33
b = 200
if b > a:
    pass# here we do not get any error.

   # FOR loop is used for iteration, over a sequence(that is either a list, a tuple, a dictionary, a set, or a string.
   # with the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

     # to print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # output: apple
                      # banana
                      # cherry
    # for loop does not require an indexing variable to set beforehand.

    # string are iterable objects, they contain a sequence of characters:

for x in "banana":
    print(x)
    '''
    output:
      b
      a
      n
      a
      n
      a

    '''


    # BREAK STATEMENT:
       # with break we can stop loop  to iterate all items.
      # exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
     print(x)
     if x == "banana":
         break
            # output : apple
                      # banana



         #  CONTINUE STATEMENT:
            # with continue we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
     if x == "banana":
         continue
     print(x)
     # output :
         # apple
         # cherry    # here we have skipped banana with continue.



     # RANGE() FUNCTION:
       # range function returns a sequence of numbers, starting from 0 by default, and increment by 1(by default), and ends at a specified number.
         # using the range() function:
for x in range(5):
    print(x) # here 5 is total numbers. from 0 - 4.
             # starting value is 0.
             # by adding parameter we can specify starting value: range(2,6) , which means values from 2 to 6 (but not including 6).

for x in range(2,6):
    print(x) # output:
                # 2
                # 3
                # 4
                # 5  # not included 6. started with 2.

     # it is possible to specify the increment value by adding a third parameter:
          # range(2.30, 3)
             # here 2 is starting point , 30 ending point , 3 is the interval between two numbers. like 2 to 5, 5 to 8.
               # increment the value by 3 (default is 1).
for x in range(2, 30, 3):
    print(x)
'''
     the output: 
2
5
8
11
14
17
20
23
26
29


    
'''



    # ELSE IN FOR LOOP:
     #ELSE keyword in a for loop specifies a block of code to be executed when the loop is finished:
       # print all the numbers from 0 to 5, and print a message when the loop has ended:
for x in range(4):
    print(x)
else:
 print("finally finished!!")  # output:

'''
output:
0
1
2
3
finally finished!!
'''

    #NESTED LOOPS:
       # nested loop is loop within loop.
          # inner loop will be executed one time for each iteration of the "outer loop":
          # print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ['apple', 'banana', 'cherry']
for x in adj:
     for y in fruits:
         print(x,y)
         '''  
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
 '''


   #PASS STATEMENT:
     # for loops can't empty so to avoid error you can use pass statement.
for x in [0,1,2]:
    pass  # here we are not getting any error message.



    # WHILE LOOP:
       # the while loop we can execute a set of statements as long as a condition is true.
          # print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1
   # output: 1,
            # 2
             #3
             #4
             #5
             # remember to increment i , or else the loop will continue forever.
'''  i = 1
    while i < 6:
        print(i)''' # this will create an infinite loop.


    # BREAK STATEMENT:
      # BY  break we can stop the loop even if the while condition is true.
       # exit the loop when i is 3.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1  # output is :   1
                           # 2
                        #  3

''' 
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
# this will create a infinite loop.

'''



  # CONTINUE STATEMENT:
     # WE CAN stop the current iteration and continue with the next:
         # eg: continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
'''  
    output is :
    1
    2
    4
    5
    6'''


 # ELSE STATEMENT:
   # THE else statement we can run a block of code once when the condition no longer is true:
   # eg:
      # print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
'''
    1
    2
    3
    4
    5
    i is no
    longer
    less
    than 6
''' # this comment line "tripel quotes should be at a proper indent otherwise it will give an error.


# PYTHON MATH MODULE:
  #  python module has a set of methods and constants:
     # math.ceil()  , rounds a number up to the nearest integer.
     # math.factorial(), returns the factorial of a number
     # math.floor() , rounds a number down to the nearest integer.
     # math.gcd() , returns the highest value that can divide two integers.
     # math.pow(x,y) , return the value of x to the power of y.
       # eg:

# import math module:
import math
a = 12.9
print("ceiling of a :=", math.ceil(a))
print("floor of a :=", math.floor(a))
b = 5
print("factorial  of b := ", math.factorial(b))
x = 2
print("value of x to the power of b:=", math.pow(x,b))
print("highest value that divide x and y: ", math.gcd(x,b))

# output:
#ceiling of a := 13
#floor of a := 12
#factorial  of b :=  120
#value of x to the power of b:= 32.0
#highest value that divide x and y:  1

