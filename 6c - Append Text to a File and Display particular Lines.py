n=int(input("enter n lines: "))
f=open('C:/Users/Hrithik/Desktop/sample.txt')
for line in (f.readlines() [-n:]):
    print(line,end="")
f.close()
