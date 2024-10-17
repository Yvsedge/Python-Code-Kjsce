'''
Write a Python program that uses lambda with filter() to select even numbers and map() to square them, 
displaying the original, filtered, and squared lists.

i = 0
numbers = []
while i == 0:
    num = int(input("Enter numbers:- "))
    numbers.append(num)
    ask = int(input("Wanna continue(0 or 1):- "))
    if ask == 0:
        break
print("Original List is :- ", numbers)
even = list(filter(lambda x : x%2 ==0 , numbers))
print("List of even number only is:- ", even)
squared = list(map(lambda x : x**2 , even))
print("List of squared even numbers is:- ", squared)
'''
'''
Write a Python program that generates a list of Pythagorean triplets (a, b, c) from a given list of integers, 
using lambda, filter(), and map(). The program should filter out invalid triplets and display valid ones.
'''
list_ol_numbers = [x for x in range(1,51)]
def pythagorean_gen(list_ol_numbers):
    py = []
    for i in list_ol_numbers:
        for j in list_ol_numbers:
            for k in list_ol_numbers:
                if i**2 + j**2 == k**2:
                    py.append((i,j,k))
    return py
py = pythagorean_gen(list_ol_numbers)
pyt = list(filter(lambda py:py[0]**2 + py[1]**2 == py[2]**2, map(sorted,py)))
for i in pyt:
    for j in pyt:
        if i == j:
            pyt.remove(j)
print(pyt)
