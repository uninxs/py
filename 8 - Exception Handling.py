try:
    num=int(input("Enter the no: "))
    re=100/num
except(ValueError,ZeroDivisionError):
    print("Something is wrong")
else:
    print("Result is",re)
