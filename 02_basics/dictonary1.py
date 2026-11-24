chai_types = {"masala": "spicy", "green": "healthy", "black": "strong"}
print(chai_types["masala"])  # Output: spicy
chai_types["masala"] = "calming" 
print(chai_types)  # Output: calming
# always value is change not  index(key)
chai_types["healthy"]="good for health" 
print(chai_types)

print(len(chai_types))  # Output: 4
x={ "name": "Riya", "age": 20, "city": "Bhopal"}
x.pop("name") 
print(x)  # Output: {'age': 20, 'city': 'Bhopal'}
print(x.popitem())  # Output: ('age', 20) jo last me add kro whi delete hoga koikry pas karne ki jroort nhi hoti hain

del x["city"]
print(x)  # Output: {}

for key in x:
    print(key)#output: name, age, city
    print(x[key])#output: Riya, 20, Bhopal
    print(key, x[key])#output: name Riya, age 20, city Bhopal


    #for key, value in x.items():
        #print(key, value)
#if "age" in x:
    #print("Age is present in the dictionary.")