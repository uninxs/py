class cl1:
    def base(self):
        print("base class")

class cl2(cl1):
    def deri(self):
        print("derived class")

c=cl2()
c.base()
c.deri()
