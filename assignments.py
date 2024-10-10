'''
Write a function power(a,b) to calculate value of ’ a’ raised to’ b’ . The
function receives a and b from user, finds the result and returns the result.
'''

def power(a, b):
    return a**b

a = int(input("Enter the value :- "))
b = int(input("Enter the power to which you want to raise the value to :- "))
result = power(a,b)
print("The value of", a , "after being is :- ", result)

#W.A.P to find power of a number using recursion

def power(a, b):
    if b != 0:
        return a * power(a, b - 1)
    else:
        return 1


a = int(input("Enter the value:- "))
b = int(input("Enter the power:- "))
print(a, "to the power", b, "is", power(a, b))

'''
Write a function to convert a decimal number to Binary number . The
function receives the decimal number from main( ) and returns the binary
number which is printed through main( ).
'''

def DecimalToBinary(num):
        if num >= 1:
            print (num % 2 , end = "")
            return DecimalToBinary(num // 2)

num = int(input("Enter the decimal whihc you want to convert to binary:- "))
binary = DecimalToBinary(num)

'''
W.A.P to print all prime numbers between two numbers (entered by the
user) by making a user-defined function.
'''
def prime(a , b):
    for i in range(a, b):
         if i == 1 or i == 0:
              pass
         elif i > 1:
            for num in range(2, i):
                if i % num == 0:
                    break
            else:
                yield i


a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
result = prime(a,b)
for j in result:
    print(j)

'''
Write a program to find sum of first n natural numbers using
recursion. Note: Positive integers are known as natural number i.e.
1, 2, 3....n
'''

def summation(n):
    if n == 1:
        return 1
    elif n > 1 :
        return n + summation(n-1)

result = summation(9)    
print(result)

'''
W.A.P to find Sum of Digits of a Number Both with and without using
Recursion
'''
#Without Recursion

def sum_of_digits(n):
    digit = str(n)
    sum = 0
    for i in digit:
        sum += int(i)
    return sum

i = int(input("enter the digit:- "))
result = sum_of_digits(i)
print(result)

#With Recursion

def sum_of_digits(n):

    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(result)


