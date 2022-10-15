def file_read(fname):
    with open(fname,'w')as myfile:
        myfile.write("python exercises\n")
        myfile.write("java exercises\n")
    txt=open(fname)
    print(txt.read())
file_read('C:/Users/Hrithik/Desktop/sample2.txt')
