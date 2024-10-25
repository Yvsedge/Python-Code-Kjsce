'''
Write a program in which we prompt users to enter personal details like name and surname, which should be strings, age should be an integer, 
and height and weight should be float. Whenever the user enters input of the incorrect type, 
keep prompting the user for the same value until it is entered correctly. Give the user sensible feedback
'''

def get_string():
    try:
        name = str(input("Enter your name:- "))
        if name.isalpha():
            return name
        else:
            raise ValueError
    except ValueError:
        print("Invalid value, Enter again")
        return get_string()
    
def get_int():
    try:
        age = int(input("Enter your age:- "))
    except ValueError:
        print("Invalid value, Enter again")
        return get_int()
    else:
        return age
    
def get_float(n):
    try:
        wight = float(input(f"Enter your {n}:- "))
    except:
        print("Invalid value, Enter again")
        return get_float(n)
    else:
        return wight
    
name = get_string()
age = get_int()
weight = get_float("weight")
height = get_float("height")

print(f"Your name is {name}")
print(f"Your age is {age}")
print(f"Your weight is {weight}")

'''
2.	Write a program to create a file employeedetails.txt" which stores the Employee details by 
adding their Employee Id, Name, and Department into it using the following format:

EmpId  	        Name	      Department
1601001          Abc          Computer
1601003          Xyz	      IT

Obtain the details for EmpId from the user.
'''

with open("employeedetails.txt", "w") as file:
    file.write("EmdId   Name    Department \n")
    flag = 0
    values = []
    while flag == 0:
        id = int(input("Enter your id:- "))
        name = str(input("Enter your name:- "))
        department = str(input("Enter your department:- "))
        file.write(f"{id}   {name}   {department} \n")
        ask = int(input("Do you want to continue(0 or 1):- "))
        if ask == 0:
            break
with open("employeedetails.txt", "r") as file:
    print(file.read())

'''
Write a program that takes a list of numbers as input from the user and calculates their average. 
If the list is empty, raise a custom exception EmptyListError with an appropriate error message.
'''
class EmptyListError(Exception):
    def __init__(self, args , Mess = "EmptyListError"):
        self.args = args
        self.Mess = Mess
        super().__init__(self.Mess)
def list_Maker():
    l1 = []
    flag = 0
    while flag == 0:
        ask = str(input("Do you want to insert value into list y or n:- "))
        if ask.lower() == 'n' or 'no':
            break
        val = int(input("Enter Value for list:- "))
        l1.append(val)
    return l1
list1 = list_Maker()
if len(list1) == 0:
    raise EmptyListError("EmptyListError")

