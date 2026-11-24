tea_type = ("green", "black", "oolong")
print(tea_type[0])  # Output: green
#tea_type[0] = "white"  # This will raise an error because tuples are immutable
print(tea_type[1])  # Output: black
print(type(tea_type))  # Output: <class 'tuple'>
print(len(tea_type))  # Output: 3

moretea_type = ("herbal", "fruit", "tisane")
print(tea_type + moretea_type)
if "green" in tea_type:
    print("Yes, green tea is available.")  # Output: Yes, green tea is available.


x=(1, 2, 3, 4,4,4, 5)
print(x.count(4))  # Output: 3

print(x.index(3))  # Output: 2


######################################################################################
t = (10, 20, [30, 40])
t[2].append(50)
print(t)

