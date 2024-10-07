'''Write a Python program using a recursive function that takes a string as input from the user and 
    displays whether the string is Palindrome.'''
'''
def palindrome(string):
    if len(string) < 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
        
string = input("Enter a string:- ")
p = palindrome(string)
if p:
    print("palindrome")
'''
'''
Write a Python program for a character frequency counter function that takes a list of strings from the user as input 
   and displays the frequency of each character in the list.'''
'''
def counter(main_list):
    string = main_list
    dict = {}
    for i in string:
        for j in range(0,len(i)):
            if i[j] in dict:
                dict[i[j]] += 1
            else: 
                dict[i[j]] = i.count(i[j])
    return dict
i = 0
main_list= []
while i == 0:
    string = input("Enter Some thing:- ")
    main_list.append(string)
    ask = input("Do you wanna continue  yor n :- ").lower()
    if ask == "n":
        break

p = counter(main_list)
non = list(p)
val = list(p.values())
print(list((non,val)))
'''
'''Alternative to 2nd'''

def take_input():
    list1 = []
    i = 0
    while i == 0:
        inp = input("Enter something: ")
        list1.append(inp)
        ask = int(input("Do you want to continue:-(0 or 1) "))
        if ask == 0:
            break
    return list1
empty = []
final = []
main_list = take_input()
for i in main_list:
    for j in i:
        p = list(map(lambda x : x.count(j) , main_list))
        empty.append((j,p))
[final.append(x) for x in empty if x not in final]
print(final, "<-- All Characters seperated for different strings")
print(" ")

total = []
for i in final:
    total.append([i[0],sum(list(filter(lambda x : (x), i[1])))])
          
print(total, "<-- total overall")
