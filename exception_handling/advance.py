'''try:
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    print(x/y)
except ZeroDivisionError:
    print("devided by zero is not allowed")
except ValueError:
    print("please enter int") 
finally:
    print("inside of finally block")
    print("devision=",x/y)
print("normal terminate")
'''

try:
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    print(x/y)
except ( ZeroDivisionError,ValueError) as msg:
    print("exception raised in try block")
    print(msg)
print("normal termination")