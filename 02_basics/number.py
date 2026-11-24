a=40.0
b=9
c=int(a)
print(c+b)#49
 

d=9.8
e=5
print(int(d)+e)#14
#int(x) variable ko change nahi karta, balki nayi value return karta hai.
#Functions jaise int(), float(), str() original variable ko 
# modify nahi karte. Ye nayi value return karte hain.
#  Agar permanent change chahiye, 
# to result ko wapas variable me assign karna hota hai:

a="chai"
b="code"
c=a+b
print(c)#+ operator string ko concatenate karta hai.
print(a,b,d,e)#comma operator space add karta hai.

print(d+8, e+2)
x=7
y=7
z=7
c=x,y,z
print(c)#as a tuple

l="chai"

print(l)#chai....print() = User ko dikhane ke liye
print(str(l))#chai.....str() = Object ko readable string me convert karne ke liye
print(repr(l))#'chai'.....repr() = Object ko printable representation me convert karne ke liye


name = "Hello\nWorld"

print(name)#hello
#world
print(repr(name))#'Hello\nWorld'



#***********************************************
print(0o10)#8
print(0o20)#16
print(0x10)#16
print(0b10)#2
print(oct(10))#0o12
print(hex(10))#0xa
print(bin(10))#0b10

print(int("12", 8))