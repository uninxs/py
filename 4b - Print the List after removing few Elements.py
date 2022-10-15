name=["Iyer","Babita","Mehta","Jethalal","Anjali"]
name=[x for(i,x) in enumerate(name) if
      i not in(0,2,4,5)]
print(name)
