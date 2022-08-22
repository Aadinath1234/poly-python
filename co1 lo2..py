# keywords in python are some reserved words/predefined keywords.
# this predefined keywords cannot be used as variable names, function names or any other identifiers.

"""
def my_func(a, b):
   c = a + b
   print(c)


my_func(10, 20)
# here def and print is a keywords.

"""


"""
keywords: and , as, assert etc.


"""


#variable : variables are like containers to store  data values.
# python do not declare variable.
# variable is created when you assign a value to it.
'''
x = 2
y = "python"
print(x)
print(y)
'''

# string variables can be declared with single or double quotes.
y = "python"
x = 'PYthon'
print(x)
print(y) # the effect is same for single and double quotes.
# a variable must  start with a letter or the underscore character
# a variable can be a simple name or a descriptive name.
# a variable name cannot start with the number.
# a variable name can only contain alpha-numeric characters and underscores.
# variable names are case sensitive(age,Age and AGE are three different variables.
# valid variable names:
   # var_name = "dj"
   # varname = "dj"
   # _var_name = "dj"
   # _varname = "aj"
   # _2varname = "dj"
   # varname_name = "dj"
   # varname2 = "dj"

# invalid variable names:
  # 2varname = "dj"
  # var-name = "dj"
  # var name = "dj"



# PYthon allows  to assign values to multiple variables in one line:
x, y, z = 'red', 'green', 'blue'
print(x)
print(y)
print(z)



# another way to write multiple variable in one line:
x , y,z = "red", "yash", "akshat"
print(x,y,z) # output: red yash akshat

# and also allows to assign same value to multiple variables:
x = y = z = "Red"
print(x)
print(y)
print(z)

# output variables:
   # the python print statement is used to output variables.
   # to combine both text and a variable, python uses the "+" character
#
x = "awesome"
print("python is " + x)
#
x = "python is "
y = "qwesome"
z = x + y
print(z)

# another way to write this :

x = " python is "
y = " awesome"
print(x+y)
# output : python is awesome



#
x = 5
y = 10
print(x+y)
# output: 15
# when you will try to combine a string and a number , python will give you an error.



# GLOBAL VARIABLES:
  #  variables that are created outside of function are known as global variables.
  # global variables can be used by everyone , both inside of function and outside.
    # create a variable outside of function and use it inside the function.

x = "awesome bhai"

def myfunc():
    print("python is " + x)

myfunc() # here x is a global variable can be accessed inside and outside of function.
#create a variable inside a function, with the same name as the global variable:
x = "awesome hai tu"

def myfunc():
    x = "fantastic"
    print("python is " + x)

myfunc()

print("python is " + x) # output:
                        # python is fantastic
                        #python is awesome hai tu

# GLOBAL KEYWORD:
 # to create a global variable inside a function , you can use the global keyword.
 # if you use the global keyword, the variable belongs to the  global scope:
def myfunc():
    global x
    x = "gulaboo"

myfunc()

print("Python  is " + x)
# the output:
             #Python  is gulaboo



#Data types:
  #python is a dynamically typed language.
  # no need to declare a variable.
  # python interpreter understood data type of variable.
  # by using type function we can find the data type of a variable.
a = 10
b = 10.5
c = "hey python!!"
print(type(a))
print(type(b))
print(type(c))
# python provides various standard data type to define storage method.
  # numbers:
     #integer
     #complex number
     #float

  #sequence type:
      # strings
      # list
      # tuple

  # boolean
  # set
  #dictionary


      # NUMBERS:
        # NUMBers stores numeric values.
        # integer , float, complex values belongs to numbers.
        #by type() function you can find the datatype of variable.
        # isinstance() function is used to check an object belongs to a particular class.
        # python creates number objects when a number is assigned to a variable.
              #eg:
a = 5
print("the type of a ", type(a))
print(" a is an integer", isinstance(5,int))
# output: the type of a  <class 'int'>
         # a is an integer True
print( isinstance(5,int))
 # the output is : true.



# python supports  three types of numeric data :
   # int :
         # interger value can be  any length such as integers 10, 1000, -10, -150
         # it has no restrictioin on length of an integer.
         # integer values belongs to 'int'.
   # float:
        # it used to store the values like 10.5, 11.7. 1.200 etc.
        # it is accurate upto 15 decimal points.
   # complex:
       # complex number contain an ordered pair i.e. x + iy where x and y are real and i is denotes imaginary part.
       # the complex number like 2.14j, 2.0 + 2.3j, etc.


# SEQUENCE TYPE:
   # string:
      # the string can be defined as the sequence of characters represented in the quotation marks.
      # we can use single, double , triple quotes to define a string.
      # in string handling , the operator "+" is used to concatenate two strigns as "hello" + " world" = "hello world".
      # the operator "*" is known as a repetition operator. such as "python" * 2 it return 'python python'.
      # examples:
str="string using double quotes"
print(str)
s = '''
       a multiline string
  '''
print(s)
# the output : #string using double
              #a multiline string

# OTHERS:
   # list : # it contain collection of members.
            # members are ordered and changeable.
            # allows duplicate members.
   # Tuple: # it is collection of members.
            # members are ordered  and unchangeable.
            # allows duplicate numbers.
   # Set:  # it is collection of members.
            # members are unordered and unindexed.
            # do not allows duplicate members.
   # Dictionary:
         # it is collection of members.
         # members are unordered, changeable and indexed.
         # do not allows duplicate members.


# TYPE CONVERSION:

x = 1
y = 2.8
z = 1j
print(x)# output : 1
a = float(x)# covert from int to float:
print(a) # output : 1.0
print(y)# output : 2.8
b = int(y)# convert from float to int
print(b) # output : 2
c = complex(x)# convert from int to complex
print(c)
print(z)# the output: 1j
#d = int(z)
#print(d)# the output: can't convert complex to int\
#e =float(z)
#print(e) # the output : can't covert complex to float.
'''
we can only convert int and float to complex data type but can't convert complex to int and float.

'''
#USER INPUT:
  # BY  this we can take inputs.
username  = input("enter username: ")
print("username is : " + username) # here after execution you have to enter again  , what you want to be print in output.


user = input(" ")
print("username is : "+ user)
# the output is :
''' kya be
 username is : 
'''




# operators:
   # operators are used to perform operations on variables and values.
   # python divides operators in :
             # Arithmetic
             # assignment
             #comparison
             # logical
             # Bitwise
             '''
            # Arithmetic operator: + , addition
                                   - , substraction
                                   * , multiplication
                                   / , divide
                                   % , modulus
                                   **, exponentiation
                                   //,Floor division
                                   this uses to perform mathematical operations.
                                    
                '''



           '''
           Assignment operator:
                =, x = 5,
                += , x+=5, x = x + 5
                -= , x-=5 , x = x - 5
                *=, x*=5, x = x * 5
                /= , x /=5, x = x/5
                %=, x %= 3, x = x % 3
                //=, x //= 3, x = x//3
                
              
           
           
           '''



           '''
           comparison operator:
             used to compare two values.
              == , equal , x == y
              !=, not equal, x != y
              > , greater than , x > y
              < , less than , x < y
              >= , greater than or equal to , x >= y
              <= , less than or equal to , x <= y
              
           
           
           
           '''



           '''
           logical operators:
              used to combine conditional statements.
              # and , returns true if both the statements are true, x < 5 and x < 10
              # or , return true if one of the statements is true, x < 5 or x < 4
              # not , reverse the result, returns false if the result is true, Not(x < 5 and x < 10)
              
           
           '''




           '''
           Bitwise operators:
            it is used to compare (binary) numbers.
           # & , AND , Sets each bit to 1, if both bits are 1.
            # | , OR,  sets each bit to 1 if one to two  bits is 1
            # ^ , XOR , sets each bit to 1 if only one of two bits is 1.
            # ~ , NOT, inverts all the bits.
            # << , zero fill left shift, shift left by pushing zeros in from the right and let the leftmost bits fall off.
            # >> , signed right shift , shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off.
            
            
           
           '''


           '''
           # IDENTITY OPERATORS:
              # used to compare the objects.
              # is,  return true if both variables are the same object, x is y.
              # is not, returns true if both variables are not the same object, x is not y
              
           
           
           '''



           '''
           # MEMBERSHIP OPERATORS:
               # used to test if a sequence is present in an object.
               # in , return true if a sequence with the specified value is present in the object, x in y.
               # not in, return true if a sequence with the specified value is not present in the object, x not in y.
               
           
           '''

           '''
           # PYTHON COMMENTS:
               this commets starts with # , ''' ''' , """ """ ,  at the end of the statement, 
           
           
           
           '''


           '''
    # USER DEFINE FUNCTION:
        # A function is a block of  program statements which can be used repetitively in  a  program.
        # we can define function as per our need.
        # function declaration  begins with this starts with the word "def", and remain will function name.
        # function may take arguments as input within the opening and closing parenthesis, just afte the function name, followed by a colon.
        # after defining the function name and arguments a block of program statements start at the next line and these
          statements must be indented.
          
           # syntax:
             def function_name(argument1, argument2, ...):
                    statement 1
                    statement 2
                    
                    
                    
              # creating a function:
                 # a function is defined using the def keyword.
                  def_function():
                    print("merabhai")
              # calling a function:
                 use the function name followed by parenthesis:
                  def my_function():
                     print("merabhai")
                     
                  my_function() # this is function calling.
                  
                  
              # Arguments:
                # information can be passed into functions as arguments.
                # arguments are specified after the function name, inside the parenthesis.
                # you can add as many arguments as you want , just seperate them with a comma.
                   def my_function(fname):
                     print(fname)
                     
                   my_function("sanjay")
                   my_function("manish")
                   my_function("durgesh")
                  
               # parameter: a parameter is the variable listed inside the parenthesis in the function definition.
               # Argument: argument is the value that is sent to the function when it is called .
               # number of arguments: no. of parameter should be equal to the no. of arguments.
                def my_function(fname, lname):
                  print(fname + " " + lname) # output : email refsnes
                  print(fname +  lname) # output: email refsnes
                my_function("email", " refsnes")  
                                         
                # my_function("email") # this will get an error , here parameter is not equal to arguments.
                
                
                
             # ARBITRARY ARGUMENTS, *args:
               # if you do not know how many arguments that will be passed into your function, add a "*" 
                 before the parameter name in the function definition.
                 by this way function will receive a tuple of arguments, and can access the items accordingly.
                 def my_function(*kids)
                    print("the youngest child is " + kids[2]
                    
                 my_function("email", " tobias", "linux")
                 # output : the youngest child is linux.
               
               # Keyword arguments:
                  # you can also send the arguments with the key = value syntax.
                   # this way the order of the arguments does not matter.
                   
                   def my_function(child3, child2, child1):
                     print("the youngest child is " + child 3)
                     
                   my_function(child1 = "email", child2 = "Tobias", child3 = "linux")
                       
                   
                # ARBITARY KEYWORD ARGUMENTS, **kwargs
                
                   # if you do not know how many keyword arguments that will be passed into your function, add two asterik: ** before the parameter name 
                      in the function definition.
                      
                      def my_function(**kid):
                         print("his last name is " + kid["lname"])
                         
                      my_function(fname = "tobias", lname = "Refsnes")
                      
                      
                      
                    #DEFAULT PARAMETER VALUE:
                        # if we call the function without argument , it uses the default value:
                           def my_function(country = "Norway"):
                              print(" I am from" + country)
                           my_function("Sweden")
                           my_function("India")
                           my_function()
                           my_function("Brazil")
                        # the output is  :    
                          
                                           I am from Sweden
                                           I am from India
                                            I am from Norway
                                             I am from Brazil



                     # passing a list as an argument:
                        # you can send any data types of arguments to a function(string, number, list, dictionary etc)
                        # it will be treated as same data type inside the function.
                       def my_function(food):
                         for x in food:
                          print(x)
                         fruits = ["apple", "banana"]
                         
                       my_function(fruits)
                       # the output is :
                            apple
                             banana
                             
                             
                  # Return Values:
                     # to let a function return a value , use the return statement.
                     def my_function(x):
                       return 5 * x
                       
                     print(my_function(3)) # output:15
                     print(my_function(4))   # output: 20          
                             
                        
                #  THE PASS STATEMENT:
                    function definition cannot be empty , but if you for some reason have a function definition
                     with no content, put in the pass statement to avoid the error.
                     def myfunction():
                        pass
                                  
                          
          '''