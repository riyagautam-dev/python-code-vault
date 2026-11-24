tea_variable=['black', 'green', 'oolong', 'herbal']
print(tea_variable[0])
tea_variable[1:2] = "lemon"
print(tea_variable)#Yahan "lemon" ke har character ko alag-alag insert kar diya gaya.
tea_variable=['black', 'green', 'oolong', 'herbal']
tea_variable[1:2]=["lemon"]
print(tea_variable)#yha lemon ko list me convert kar diya gaya hai.



print(tea_variable[1:1])#ye empty list return karega
tea_variable=['black', 'green', 'oolong', 'herbal']
tea_variable[1:1]=["lemon", "masala"]
print(tea_variable)#yha lemon aur masala ko list me convert kar diya gaya hai.


#Ye exactly list.insert() ki tarah behave karta hai.
tea_variable = ['black', 'green', 'oolong', 'herbal']
tea_variable.insert(3, "ginger")
print(tea_variable)
tea_variable[1:3] = []
print(tea_variable)



tea_variable_coppy = tea_variable.copy()# memory allocation alag ho gayi hai
