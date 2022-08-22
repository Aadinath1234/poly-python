thislist = ["apple","banana","cherry"]
#print(thislist[-3])
#print(thislist[1])
#print(thislist[2])
#print(thislist[0])
#print(thislist[0:1])
#print(thislist[2:])
"""thislist[0] = "yashwardhan dugaya"
print(thislist)"""
"""thislist[1] = "akshat uprit"
print(thislist)"""
thislist.append("vicky dugaya")
print(thislist)
thislist.append("aadesh")
print(thislist)
thislist.insert(0, "mango")
print(thislist)
thislist.insert(3,"rishabh")
print(thislist)
thislist.remove("rishabh")
print(thislist)
thislist.remove("vicky dugaya")
print(thislist)
thislist.pop()
print(thislist)
thislist.pop(0)
print(thislist)










del thislist[1]
print(thislist)
#del thislist (deletes whole list)
thislist.clear()
print(thislist)# empties whole list  , clearlist





yash = ["dikhawa", "dhong", "pakhand"]
for x in yash:
    print(x)

vicky = ["akshat", "rishabh", "chirag"]
for y in vicky:
    print(y)


if "aadesh" in vicky:
    print("ha akshat likha hai list me")
else:
    print("nahi likha hai bhai")



print(len(thislist))
print(len(vicky))
print(len(yash))



syn = vicky.copy()
print(syn)

syn = list(vicky)
print(syn)

# to add lists:
list1 = ['a', 'b']
list2 = ['c','d']
list3 = list1 + list2
print(list3)


for x in list2:
    list1.append(x)
    print(list1)


list1.extend(list2)
print(list1)

#Sorting:
cars = ['ford','bmw','volvo']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

fruits = ["apple", "banana", "orange"]
fruits.reverse()
print(fruits)


#string

a = "hello  rt"
print(a[0])

b = "Hello,world"
print(b[2:6])
print(len(b))