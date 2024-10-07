#Write a python program to take list values as input parameters and returns another list
#without any duplicates.
flag = 0
list1 = []
while flag == 0:
    i = input("Enter items that you want to insert in a list:- ")
    list1.append(i)
    ask = input("do you want to continue y or n:- ").lower()
    if ask == "n":
        break
print(list1)
sets = set(list1)
list1 = list(sets)
print(list1)

#Second Question, Count the frequency of characters of a string and display it as a dictionary
string = input("Enter the string:- ")
dict   = {}

for i in range(len(string)):
    dict[string[i]] = string.count(string[i])

print(dict)
