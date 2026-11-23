#In Python, mutable objects can have their values modified in place after creation, whereas immutable objects cannot be changed.
#  Examples of mutable objects include lists, dictionaries, sets, and bytearrays.
#  Examples of immutable objects include integers, floats, strings, tuples, and frozensets.
#  The real meaning of immutable is that once an object of an immutable type is created, its value cannot be changed in memory if i taken an example that userame=riya or kanhiya so riya does not change but the object itself remains the same and username point other values.
username = "shreya"
print (username)
x=15

y=x
print (y)#15
print (x)#15
print (id(y))
print (id(x))
x=20
print (x)#20
print (y)#15
#this shows that x and y are two different objects in memory. When we change the value of x, it does not affect the value of y because integers are immutable in Python.
print(id(x))# Memory address of x is different from the memory address of y
print(id(y))
#id shows the memory address of the object. When we change the value of x, it points to a new memory address, while y still points to the original memory address.