'''
1) Program to Calculate the Sum of n Natural Numbers. Read the value of n from the
user.
'''
n = int(input("Enter the n:- "))
result = sum([i for i in range(1,n+1)])
print(result)

'''
2) Program to Find Factorial of a Number entered by the user
'''
fact = int(input("Enter a number hose factorial you want to find "))
mult = fact
for n in range(1, fact):
    mult *= fact-n
print("factorial of ", fact , "is - ", mult)
'''
3) Program to Generate Multiplication Table of a number entered by the user
'''
number = int(input("Enter the number whose multiplication table you want:- "))
for i in range(1, 11):
    print("{}x{} = ".format(number,i), number*i)

'''
4) Program to Display Fibonacci Sequence for n terms. Read the value of n from the user.
'''
limit = int(input("Enter the number of fibonacci terms you want :- "))
a = 0
b = 0
c = 1
for i in range(0,limit):
    print(c)
    c = c+a
    a = c-b
    b = a

'''
5) Program to find sum of elements in a given array
'''
flag = 0
arr = []
while flag == 0:
    val = int(input("Enter value for array:- "))
    arr.append(val)
    ask = int(input("Do you want to continue:-(0 or 1) "))
    if ask == 0:
        break
result = sum(map(lambda x: x, arr))
print(result)
'''
6) Program to find largest element in an array
7) Program to Reverse a Number

'''
