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
print(result)
