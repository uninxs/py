#practical 1 dateandtime
'''import datetime
name=input("entr name")
print("hello",name)
age=int(input("enter age"))
year_now=datetime.datetime.now()
print("you will turn 100 in" + str(int(100-age)+ int(year_now.year)))'''



#practical 2 even or odd

'''num=int(input("enter a number"))
if (num%2) ==0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))'''
    
    
    
    
#practical 3 Program to display the Fibonacci sequence up to n-th term
'''nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1  '''
         
#reverse of a number
'''num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))'''



# Factorial of a number using recursion
'''def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input("enter a number"))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))'''
   
   
   
   #finds vovel in string
'''def find_vovel(s):
    a = ['a','e','i','o','u']
    for i in s:
        if i in a:
            print('true')
        else:
            print('False')    
s = "God Is Great"
find_vovel(s)'''


#length of a string
'''def len_s(s):
    count = 0
    for i in s:
        if i!=' ':
            count+=1
    print('the total length of string is', count)
s ='hello python' 
len_s(s)'''

#histogram

'''def histogram(ll):
    for i in ll:
        print('*'*i)
ll = {4,7,3,5}
histogram(ll)'''        


#Check wether pangram of not
'''import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram('The quick brown fox jumps over the lazy dog'))'''




#print all elements in the list that are less than 5

'''a=[1,1,2,3,5,8,13,21,34,55,89]
for i in a:
 if i<5:
  print(i)'''
  
  
  
#CLONE OR COPY A LIST

'''L1=[8,11,13,22,27]
l2=list(L1)

print("L1:",L1)
print("L2:",l2)'''


#specified list after removing the n term
'''name=["A","B","C","D","E","F","G","H"]
name=[x for(i,x)in enumerate(name)if i not in (0,2,4,5)]

print(name)'''



#atleast one common element
'''l1=[1,2,3,4,5,6,] 
l2=[11,12,13,14,15,6] 
for i in l1: 
 for j in l2: 
 if i==j: 
 print ('The 2 list have at least one common element')'''
 
 
 
 
 
 #sorting a dictionary by value

'''import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)'''



#concatenating dictionaries
'''dict1={1: 10,2: 20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)'''


#sum all items in a dictionary
'''d={1: 10,2: 5,3: 25}
print (d)
print('sum:',sum (d.values() ))'''


#Inheritance
'''class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  '''


#try except statements
'''a = ["Python", "Exceptions", "try and except"]  
try:  
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
     for i in range( 4 ):  
        print( "The index and element from the array is", i, a[i] )  
#if an error occurs in the try block, then except block will be executed by the Python interpreter       
except:  
    print ("Index out of range")  '''
    
    
 #widget with bg red
'''import tkinter 
from tkinter import * 
root=Tk() 
O=Canvas(root,bg="red",width=500,height=500) 
O.pack() 
n = Label(root,text="Hello World") 
n.pack() 
root.mainloop()   '''



#messages
'''from tkinter import * 
root = Tk() 
var = StringVar() 
label = Message( root, textvariable=var, relief=RAISED ) 
var.set("Hey!? How are you doing?") 
label.pack() 
root.mainloop()'''


#Button in Python 

'''from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()'''

#Entry in Python 
'''from tkinter import * 
top = Tk() 
L1 = Label(top, text="User Name") 
L1.pack( side = LEFT) 
E1 = Entry(top, bd =5) 
E1.pack(side = RIGHT) 
top.mainloop()'''

#CheckButton In Python 
'''from tkinter import * 
from tkinter import messagebox
import tkinter 
top = tkinter.Tk() 
CheckVar1 = IntVar() 
CheckVar2 = IntVar() 
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \ 
                 onvalue = 1, offvalue = 0, height=5, \ 
 width = 20) 
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \ 
onvalue = 1, offvalue = 0, height=5, \ 
 width = 20) 
C1.pack() 
C2.pack() 
top.mainloop()'''



#RadioButton in Python 
'''from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()'''



# Python program to demonstrate scale widget

'''from tkinter import *
root = Tk()
root.geometry("400x300")

v1 = DoubleVar()

def show1():	
	sel = "Horizontal Scale Value = " + str(v1.get())
	l1.config(text = sel, font =("Courier", 14))
s1 = Scale( root, variable = v1,
		from_ = 1, to = 100,
		orient = VERTICAL)
l3 = Label(root, text = "Horizontal Scaler")
b1 = Button(root, text ="Display Horizontal",
			command = show1,
			bg = "yellow")
l1 = Label(root)
s1.pack(anchor = CENTER)
l3.pack()
b1.pack(anchor = CENTER)
l1.pack()

root.mainloop()'''



#rdyyn yhtnytr
'''import mysql.connector
db=mysql.connector.connect(user='root',passwd='root',host='127.0.0.1',database='n
it') 
# prepare a cursor object using cursor() method 
cursor = db.cursor() 
# Drop table if it already exist using execute() method. 
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE") 
# Create table as per requirement 
sql = """CREATE TABLE EMPLOYEE ( 
 FIRST_NAME CHAR(20) NOT NULL, 
 LAST_NAME CHAR(20), 
 AGE INT, 
 SEX CHAR(1), 
 INCOME FLOAT )""" 
cursor.execute(sql) 
print("Table Created Successfully"); 
# disconnect from server 
db.close()'''

