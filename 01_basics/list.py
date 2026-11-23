#List Python ka ordered, mutable (changeable) data structure hai jo multiple values ko ek variable me store karta hai.
#collection of hetrogeneous elements,
fruits = ["apple", 1, "mango"]
print(fruits)
#List ko create karne ke baad modify kar sakte hain.
numbers = [10, 20, 30]
numbers[1] = 25

print(numbers)  # Output: [10, 25, 30]
#Allows Duplicates
colors = ["red", "blue", "green", "red"]  # "red" is duplicated
#Positive indexing:
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


#Negative indexing:
print(fruits[-1])

#Slicing
#list[start:stop:step]
nums = [10,20,30,40,50]

print(nums[1:4])

#Adding Elements
#append()
# #End me element add karta hai.
nums = [1,2]

nums.append(3)

print(nums)
#####################################################
mylist = [1, 2, 3,"chai"]
len(mylist)  # 4


mylistone=[1, 2, 3, "chai"]
mylisttwo=mylistone
mylistone[0]="coffee"
print(mylistone)
print(mylisttwo)  # Output: ['coffee', 2, 3, '



mylistone = [1, 2, 3, "chai"]
mylisttwo = mylistone.copy()

mylistone[0] = "coffee"

print(mylistone)
print(mylisttwo)


#mutable me dono bdlenee
#immutable me dono alag alag rahenge
# m is n dekht ahai ki same memory allocation hai ya nahi