my_love={"name": {"first_name": "Raj", "last_name": "Sharma"}, "age" :{"current_age": 25, "birth_year": 1998}}
print(my_love)
print(my_love["name"]["first_name"])  # Output: Raj
print(my_love["age"])

square_num = {x: x**2 for x in range(10)}
print(square_num)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
square_num.clear()  # Output: {}
print(square_num)  # Output: {}


keys=["name", "age", "status"]
default_values="unknown"
new_dict=dict.fromkeys(keys, default_values)
print(new_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'status': 'unknown'}


keys=["name", "age", "status"]
values=["Raj", 25, "Single"]
print(dict(zip(keys, values)))

