username="riya"
print(len(username))
print(username[0])#r
#username[1]='q'# does not support because string is immutable
print(username[-1])#a because negative indexing is supported in python and access from last index
print(username[1:3])#iy because slicing is supported in python and access from 1 to 2 index
print(username[0:3])#riy because slicing is supported in python and access from 0 to 2 index
print(username[0:4])#riya because slicing is supported in python and access from 0 to 3 index
print(username[0:2:3])#r because slicing is supported in python and access from 0 to 1 index with step 3
#[start,stop,step] step is optional and default value is 1
username[0:4:1]  # riya
username[0:4:2]  # ry
username[0:4:3]  # ra
username[1:4:2]  # ia