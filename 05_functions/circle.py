pi = 3.14159
def circle_area(radius):
    return pi * radius ** 2
print("Area of circle with radius 5:", circle_area(5))
def circle_circumference(radius):
    return 2 * pi * radius
print("Circumference of circle with radius 5:", circle_circumference(5))

#######################################################
import math

def circle_area(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circle_area(7)

print("Area of circle with radius 7:", round(area, 2))
print("Circumference of circle with radius 7:", round(circumference, 2))