#Dictionary Python ka key-value pair data structure hai.

#Keys unique hoti hain.
#Values duplicate ho sakti hain.
#Dictionary mutable (changeable) hoti hai.
#Python 3.7+ me insertion order maintain hota hai.


student = {
    "name": "Riya",
    "age": 20,
    "city": "Bhopal"
}

print(student)

#Accessing Values
student = {
    "name": "Riya",
    "age": 20
}

print(student["name"])

#Using get()
print(student.get("age"))

#Adding New Items
student = {
    "name": "Riya",
    "age": 20
}
student["city"] = "Bhopal"
print(student)


#length of dictionary
print(len(student))