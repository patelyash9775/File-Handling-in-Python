
with open("file3.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("We are fine")
myfile.close()