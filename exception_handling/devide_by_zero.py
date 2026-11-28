def devide(x,y):
    try:
        z=x/y
        print("divison=",z)
    except ZeroDivisionError:
        print("sprry you are diving by 0")
#main
print("start")
devide(1,8)
devide(8,8)
devide(1,0)
devide(8,0)
devide(1,6)
print("end")