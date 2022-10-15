#def factorial(x):
#    """This is a recursive function
#    to find the factorial of an integer"""
 #  if x == 1:
#        return 1
 #   else:
        # recursive call to the function
 #       return (x * factorial(x-1))

#num = 7









# Python 3: Fibonacci series up to n
#
# >>> def fib(n):
#>>>     a, b = 0, 1
#>>>     while a < n:
#>>>         print(a, end=' ')
#>>>         a, b = b, a+b
#>>>     print()
#>>> fib(1000)








# function which return reverse of a string
def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")










