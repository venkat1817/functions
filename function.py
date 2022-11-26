'''
age=int(input("enter a your age:"))
if age>=18:
        print("your eligible to vote")
else:
        print("you not eligible to vote")                     #output:
                                                                      enter a your age:20
                                                                     your eligible to vote
                                                                     
'''

#python function basic programs.

#wap to find the highest number of two given numbers?
'''
n1=eval(input("enter a first number:"))
n2=eval(input("enter a second number:"))
                                                #(a,b)---->formal/positional arguments.
def display(a,b):                               #def----> is a python key word.
    if a>b:
        print('{} is highest number {}and{}.format(a,a,b)')
    else:
        print('{} is highest number {}and{}.format(b,a,b)')
display(n1,n2)                                                #n1,n2 ---->actual arguments.
                                                              #display---->means function call.
'''
#wap reapeat a name in function ?*****
'''
def namerepeat(n,s='NTH'):    #n---> is non-defult value
    for i in range(n):        #s='NTH'---->is defult value
        print(s)             #5---->non-key word argument 
    namerepeat(5)
'''
#wap reapeat a name in function diffent types in argument?*****
'''
def namerepeat(n,s):    
    for i in range(n):        
        print(s)        
    namerepeat(3,'NTH')
    namerepeat(10,'NTH')
    namerepeat(100,'NTH')
    
'''
#wap reapeat a name in function diffent types in argument?*****
'''
def namerepeat(n,s):    
    for i in range(n):        
        print(s)        
namerepeat(3)
namerepeat(10)
namerepeat(100)
'''

#wap to fetch all even numbers from given list?
'''
lst1=[10,4,5,7,8,9,3]
def fetchevennumber(lst1):
    lst2=[]                #create one list2 in even numbers.
    for i in lst1:
        if i%2==0:
            lst2.append(i)
    print(lst2)
fetchevennumber(lst1)                                         #output:
                                                                     [10, 4, 8]
                                                                     
'''
#wap to fetch all even numbers from given list?
'''
lst1=[10,4,5,7,8,9,3]
def fetchevennumber(lst1):
    for i in lst1:
        if i%2==0:
            print(i)
fetchevennumber(lst1)                                #output:
                                                             10
                                                              4
                                                              8

'''
#wap to fetch all vowels from the given string?
'''
st=input('enter a string:')
def fetchingvowels(st):
    lst=[]
    for i in st:
        if i in 'aeiou':
            lst.append(i)
    print(lst)
fetchingvowels(st)                                      #output:
                                                               enter a string:'narayana'
                                                               ['a', 'a', 'a', 'a']
'''
#wap to fetch all 3 divisibles from list.
'''
lst=[12,4,9,7,6,15]
def fetchthreedivisible (lst):
    lst1=[]
    for i in lst:
        if i%3==0:
            lst1.append(i)
            print(lst1)
fetchthreedivisible (lst)
                                                                 #output:
                                                                 [12]
                                                                 [12, 9]
                                                                 [12, 9, 6]
                                                                 [12, 9, 6, 15]
'''

#wap to find the square of every number in the given list.
'''
lst=[2,5,4,7,6]
def findthesqure(lst):
    lst1=[]
    for i in lst:
        x=i**2
        lst1.append(i)
        print(lst1)
findthesqure(lst)
                                                              #output:
                                                              [2, 5]                                                      
                                                              [2, 5, 4]
                                                              [2, 5, 4, 7]
                                                              [2, 5, 4, 7, 6]   

'''

#write aprogram to filter all numbers which is even number and divisible by 3?
'''
lst1=[10,12,16,6,20]
def filterallnumber(lst1):
    lst2=[]
    for i in lst1:
        if i%3==0:
         lst2.append(i)
        print(lst2)
filterallnumber(lst)                               #opt:12,6
'''

#wap to filter all odd numbers into new list.
'''
lst=[3,5,2,8,13,43,22]
def FilterAllOddNums(lst):
    lst2=[]
    for i in lst:
        if i%2==1:
            lst2.append(i)
            print(lst2)
FilterAllOddNums(lst)                           #output:
                                                [3]
                                                [3, 5]
                                                [3, 5, 13]
                                                [3, 5, 13, 43]
'''