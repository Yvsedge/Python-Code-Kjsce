import math

#Write a program to find out whether a number is even or odd.

number = int(input("Enter a number:- "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Write a program to find out whether input alphabet is a vowel or not.

i = str(input("Enter a alphabet:- "))
vowels = ['a','e','i','o', 'u']
if i in vowels:
    print("alphabet is vowel")
else:
    print("consonant")

'''
In a company, an employee is paid as per the following rules-
    I. If his Basic salary is less than Rs 15000 then HRA=10% and DA=90% of
       Basic Salary respectively.
    II. If his Basic salary is equal to or above Rs 15000 then HRA=Rs1700 and
        DA=98% of Basic Salary respectively.
If the employees salary is read through the keyboard. 
Write a program to find his gross salary
'''
b_salary = int(input("Enter your salary:- "))
HRA      = 0
DA       = 0
g_salary = b_salary + HRA + DA
if b_salary < 15000:
    HRA = .1*b_salary
    DA  = .9*b_salary
    g_salary = b_salary + HRA + DA
    print("Gross salary of the employee is:- ", g_salary)
else:
    HRA = 1700
    DA  = .98 * b_salary
    g_salary = b_salary + HRA + DA
    print("Gross Salary is:- ", g_salary)

'''
While purchasing certain items, a discount of 10% is offered if the quantity
purchased is more than 1000. If Quantity and price per item are read from the user.
Write a program to calculate the total expense
'''
cost = int(input("Enter cost per item:- "))
quantity = int(input("Enter quantity of item:- "))
discount = 0
total = cost * quantity
total_cost = 0
if quantity > 1000:
    total_cost = total * .1
else:
    total_cost = total
print(total_cost)

'''
Given a point (x,y). 
WAP to find out if the point lies on the X axis or Y axis or on the origin.
'''
x = int(input("Enter x coordinate:- "))
y = int(input("Enter y coordinate:- "))
if x == 0 and y == 0:
    print("Origin")
elif x == 0 and y != 0:
    print("Y axis")
elif x != 0 and y == 0:
    print("X axis")
else:
    print("The Coordinate of the point is:- ", (x,y))

'''
Given three points (x1,y1),(x2,y2) and (x3,y3). 
WAP to check if all the 3 points fall on one straight line or not.
'''
x1 = int(input("Enter x coodinate 1:- "))
y1 = int(input("Enter y coodinate 1:- "))
x2 = int(input("Enter x coodinate 2:- "))
y2 = int(input("Enter y coodinate 2:- "))
x3 = int(input("Enter x coodinate 3:- "))
y3 = int(input("Enter y coodinate 3:- "))
cood1 = (x1,y1)
cood2 = (x2,y2)
cood3 = (x3,y3)
if math.atan(y1/x1) == math.atan(y2/x2) == math.atan(y3/x3):
    print("Collinear")

#WAP to check whether the triangle is isosceles, equilateral or scalene.
a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid side lengths")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


