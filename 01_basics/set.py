a={1, 2, 3}
b={3, 4, 5}
print(a & {2, 3, 4})  #intersection
print(a | {2, 3, 4})  #union
print(a - {2, 3, 4})  #difference
print(a ^ {2, 3, 4})  #symmetric difference
print(a-{1,2,3})  #empty set represent by set() function not{ } because this is disctonary
a.add(10)# add karne ke liye
print(a)
a.update(b)
print(a)#Do sets ko merge karta hai.

(a.remove(7))#agar element exist nahi karta hai to error dega
print(a)
(a.discard(3))#agar element exist nahi karta hai to error nahi dega
print(a)
