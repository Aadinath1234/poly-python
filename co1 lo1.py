# indentation should be atleast one , maximum can be taken as choice of programmer .
# you have to use same number of spaces in the same block of code, otherwise it was an error.
if 4 > 2:
    print("yes it is")
     print("na baba na ") # so the output is an error, an indentation error.
# python comments can be :
   # it can start with "#" hash symbol
   # or a multiline comment with single quotation and multiple quotation(3 times) up and down.
   # this comments can be place at the end of the line.`

# modules :
    # modules works as a code library of functions, class , variables
    # a running code.
    #it is consists of python code.
    # it contain a set of functions you want to include in your application.
    # this code is in file named joker.py
    '''def message(name):
            print("welcome to "+name)'''
    # we used this joker file by importing in another file named jugnoo
      '''import joker
          joker.message("python")'''
        '''
        the output of this code is 
         # welcome to python'''
         '''
         import joker as dj
        dj.message("python")''' # you can take module name in short form or other name by taking "as" .it will work same as before.


       # syntax of module , module_file_name.function_name.


 # pythonpath:
'''a = 2
  2 is an object stored in memory , name associate  with it as "a".
'''
"""
a = 2
print("id(2)=",id(2))
print("id(a)=",id(a))
output:id(2)= 140709969376112
       id(a)= 140709969376112
       both refers to the same object 2. they have the same id()


"""

'''a = 2
print('id(a) = ', id(a))
a = a+1
print('id(a) = ', id(a))
print('id(3) = ', id(3))
b = 2
print('id(b) =', id(b))
print('id(2) = ', id(2))
'''


# namespace is a collection of names , it is a system to have unique name for each and every object in python.
# the object can be a variable ,a method or a class.
# the role of the namespace is like surname .
# name = a name , unique identifier, space = related to scope, or it depends upon the location from where is trying to access a variable or a method.
# scope is a portion of program from where a namespace can be accessed directly without any prefix.
# three variable scopes:
            # local namespace
            # global namespace
            # built-in namespace
            '''
 """           
def outer_function():
   b = 20
   print("b:=", b)

a = 10
outer_function()
print("a:=",a)

here b is in local namespace and a is in global namespace of outer_function()    
            
"""


'''
#examples of scope and namespace in python
#three different variables a  are defined in separate namespaces and accessed accordingly.
def outer_function():
   a = 20
   def inner_function():
      a = 30
      print('a = ', a)

   inner_function()
   print('a = ', a)


a = 10
outer_function()
print('a = ', a)


'''

'''
# example of scope and namespace in python
# all refrences and assignments are to the global a due to the use of keyword global.

def outer_function():
   global a
   a = 20
   def inner_function():
     global a
     a = 30
     print('a =', a)

   inner_function()
   print('a = ', a)

a = 10
outer_function()
print('a =', a)

'''



# datetime module :
   # a date in python is not a data type of its own
   # using a module named datetime to work with dates as date objects.
'''
import datetime
x = datetime.datetime.now()
print(x) #this displays the current date.
# the output is = 2021-12-29 18:34:15.726434, this date contain year, month, day,hour,minute,second,and microsecond.
# to return information about the date object
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# creating date objects:
  # to create a date we can use the datetime() class(constructor) of the datetime module.
  # the datetime() , class requires three parameters to create a date: year , month, day.
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)  # the output is : 2020-05-17 00:00:00
  # the datetime() class also takes parameters for time and timezone(hour,minute, second, microsecond,tzone), but they are optional(set default zero).


# strftime() method:
   # datetime object has a method for formatting date objects into readable strings.
   # this method is called strftime(), and takes one parameter, format to specify the format of the returned string.
   # to display the name of the month
import datetime
x= datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) # the output is : JUne
'''

