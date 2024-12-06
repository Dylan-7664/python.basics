#functions
from datetime import date


def cal_area_triangle(b, h):
    area = 0.5 * b * h
    print(area)


def cal_area_circle(radius):
    area = 22/7 * radius * radius
    area=round(area,2)
    print("Area of circle is", area,"cm^2")

def print_todays_date():
    todays= date.today()
    print("Today's date is", todays)

def add(*args):
    total=0
    for num in args:
        total += num
        print("tOtal is ", total)


def sayHi(name, age=21):
    print("Hello " + name + ", I am " + str(age) + " years old.")

sayHi('Mary')
sayHi('kevo',20)


#use a func==calling
cal_area_triangle(8, 13)
cal_area_triangle(16, 40)

triangles = [[8, 9], [9, 7], [4, 12], [3, 6], [13, 6]]

for triangle in triangles:
    cal_area_triangle(triangle[0], triangle[1])

cal_area_circle(28.73653)
print_todays_date()

add(1,2)
add(12,22,46,78,56,34,13,55)
add(74,56,65,24,74,23,12)

#data name phone gender amaoun
#account
#deposit withdrawal check balance
#oop
#----------------------



