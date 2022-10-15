def find_common(st1,st2):
    res=False
    for x in st1:
        for y in st2:
            if x==y:
                res=True
                return res
print(find_common([4,6,8,10,12],[5,7,8,10,11]))
print(find_common([3,5,7,9,11],[2,4,6,8]))
