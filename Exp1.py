'''

Write a python program to calculate salary of an employee given his basic pay (to be entered by user), 
HRA = 10 percent of basic pay, TA = 5 percent of basic pay. 
Define HRA and TA as constants and use them to calculate the salary of the employee.

'''

basic_salary = int(input("Enter your basic salary:- "))
TA           = 0.5*basic_salary
HRA          = 0.3*basic_salary
Total_salary = TA + HRA + basic_salary
print("Total Salary is :- ", Total_salary)

'''
Second Quetion
'''
#Create a variable and assign "Python programming" to it

string = "Python programming"

#access "i" using index

loc = string.index("i")
print(string[loc])

#find the lenght of the string

print("Lenght of the string is :- ", len(string))

#Slice "Python" and print it

print(string[string.index("P"):string.index("n")+1])

#slice "program" and print it

print(string[string.index("program"):string.index("m")+1])

#get the "thing" from the variable

print(string[2] + string[3] + string[-3] + string[5] + string[-1])

#convert string into uppercase

print(string.upper())

string2 = "is interesting"
print(string + " " + string2)

#apply different string methods

print(string.isnumeric())
print(string.isalpha())
print(string.isspace())
print(string.isalnum())
print(string.istitle())
print(string.isprintable())
print(string.isidentifier())
print(string.islower())
print(string.isupper())
print(string.capitalize())
print(string.index("p"))
print(string.find("p"))
print(string.title())
print(string.casefold())
print(string.replace("Python", "java"))
print(string.count("P"))
print(string.endswith("g"))
print(string.partition(" "))
print(string.split())
