# to create a class:
class MyClass:
    x = 5
    y = 15
p1 = MyClass()
print(p1.x)
print(p1.y)



# __init__function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+ self.name +  "and my age is " + self.age)

p1 = Person("john" ,   "36")
p1.myfunc()


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("your name is " + abc.name +" & your age is " + abc.age)


p1=Person("john", "38")
p1.myfunc()



#to modify:
p1.age = "40"
p1.myfunc()

class yash:
    pass