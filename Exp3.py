'''
Write a program to read the numbers until -1 is encountered. 
Also, count the number of prime numbers and composite numbers entered by the user
'''

i = 0
l1 = []
prime = []
compo = []
while i == 0:
    num = int(input("Enter number:- "))
    l1.append(num)
    ask = int(input("Do you want to continue 0 or 1:- "))
    if ask == 0:
        break


for i in l1:
    if i == -1:
        break
    if i == 1 or i == 0:
        pass
    for j in range(2 , i):
        if i%j == 0:
            compo.append(i)
            break
    else:
       prime.append(i)
print(prime, compo)
print("No of prime:- ", len(prime))
print("No of composite:- ", len(compo))

'''
Write a program to check whether a number is Armstrong or not.
(Armstrong number is a number that is equal to the sum of cubes of its digits for example: 153 = 1^3 + 5^3 + 3^3.)
'''

arm = int(input("Enter a number:- "))
p = str(arm)
sum = 0
for i in p:
    sum += int(i)**len(p)
    if sum == arm:
        print("Number is an armstrong number")
