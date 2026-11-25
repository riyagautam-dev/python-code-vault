def sum(number1,number2):
    return number1+number2
result=sum(10,20)
print("The sum of 10 and 20 is:", result)
#######################################
def sum(a, b):
    return a + b

print(sum(2.5, 3.5))
#################################33
def sum(a, b):
    return a + b

print(sum("Hello ", "Riya"))
###################################3333
def sum(a, b):
    return a + b

print(sum([1,2], [3,4]))
###################################3\
def sum(a: int, b: int) -> int:
    return a + b
#ye btata hai ki a aur b int type ke hone chahiye aur return value bhi int type ka hoga
#⚠️ Lekin dhyan rahe: Type hints documentation aur editor ki help ke liye hote hain. Python by default unhe enforce nahi karta.
# c me int a likhtw hai kyuki Compiler pehle hi check karta hai "Kya a integer hai?"
#jbki payton bolte gai run yime me dekh luga ky hai Isi liye Python dynamic typing use karta hai.
