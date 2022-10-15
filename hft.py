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

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# gene fib seq
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1'''
       
       


#reverse of a number

'''
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))'''


#armstrong or palindrome
# Python program to check if the number is an Armstrong number or not

# take input from the user
'''num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''
   


# Python program to check if the number provided by the user is an Armstrong 
'''number or not 
defarmstrong(num): 
 sum=0 
 # find the sum of the cube of each digit 
 temp = num 
 while temp > 0: 
 digit = temp % 10 
 sum += digit ** 3 
 temp //= 10 
 # display the result 
 if num == sum: 
 print(num,"is an Armstrong number") 
 else: 
 print(num,"is not an Armstrong number") 
def palindrome(num): 
 n = num 
 rev = 0 
 while num != 0: 
 rev = rev * 10 
 rev = rev + int(num%10) 
num = int(num / 10) 
 if n == rev: 
 print(n,"is palindrome number") 
 else: 
 print(n,"is not a palin") 
# take input from the user 
num = int(input("Enter a number to chk it is armstrong or not: ")) 
armstrong(num) 
# take input from the user 
num = int(input("Enter a number to chk it is palindrome or not: ")) 
palindrome(num)'''




'''def find_common(str1,str2):
    res=False
    str1=(4,6,8,10,12,5,7,8,10,11)
    for x in st1:
     for y in st2:
         if x==y:
             res==true
             return res
str1=(4,6,8,10,12,5,7,8,10,11)         
print(find_common([4,6,8,10,12],[5,7,8,10,11]))
print(find_common([3,5,7,9,11],[2,4,6,8]))'''
        
        
        
#CLONE OR COPY A LIST

'''L1=[8,11,13,22,27]
l2=list(L1)

print("L1:",L1)
print("L2:",l2)'''

#atleast one common element
'''l1=[1,2,3,4,5,6,] 
l2=[11,12,13,14,15,6] 
for i in l1: 
 for j in l2: 
 if i==j: 
 print ('The 2 list have at least one common element')'''
 
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  