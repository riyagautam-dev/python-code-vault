def student(**kwargs):
    print(kwargs)

student(name="Anurag", age=21, city="Bhopal")
######################################################3


def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Anurag", age=21, city="Bhopal")

##################################33
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(10, 20, 30, name="Anurag", city="Bhopal")