def square(number):
    return number * number
result=square(5)
print("The square of 5 is:", result)


################################


def square(number):
    print("The square of", number, "is:", number **2)
    square(5)