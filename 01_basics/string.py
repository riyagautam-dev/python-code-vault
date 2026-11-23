chai="masala chai"
chai_first=chai[0]
print(chai[0])

slice_chai=chai[0:6]
print(slice_chai)
slice1_chai=chai[7:11]
print(slice1_chai)

print(chai.lower())
print(chai.upper())

str="          Hello    World       "
print(str.strip())#strip() function space hata deta hai

#Sabhi spaces hatane hain
name = " Hello   World "

print(name.replace(" ", ""))
print(name.replace("World", "Python"))#replace() function string me se replace kar deta hai
print(name)


a= "Hello , riya , how are you"
print(a.split())#split() output shi se nhi dega 
print(a.split(","))#split() function string ko list me convert kar deta hai
b= "Hello_riya_how are you"
print(b.split("_"))

print(" ".join(b.split("_"))) # join() function list ko string me convert kar deta hai

#********************************************************************
"-".join(["A", "B", "C"])   # A-B-C

",".join(["A", "B", "C"])   # A,B,C

" ".join(["A", "B", "C"])   # A B C

"".join(["A", "B", "C"])    # ABC

"***".join(["A", "B", "C"]) # A***B***C


school="St.Joseph's School"
print(school.find("School"))#-1 returns -1 if the substring is not found, otherwise returns the index of the first occurrence of the substring.


chai2="masala chai chai chai chai"
print(chai2.count("chai"))#4

chai_type="masala chai"
quantity=5
order="I want to order {} cups of {}"
print(order.format(quantity, chai_type))


age = "twentyfive"

for letter in age:
    print(letter)

path = "C:\\Users\\anura\\OneDrive\\Desktop\\python\\01_basics\\list.py"
print(path)

path1="riya\"hello\""
print(path1)

masala_chai=r"masala\chai" # r prefix ka use karne se string me jo bhi escape characters hote hain unhe ignore kar deta hai aur last me \ ata h ton problem create hoti h.
print(masala_chai)

print("masala" in "masala chai")
