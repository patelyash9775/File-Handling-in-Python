file=open("Temp_file.txt",'a')
s=input("Enter a information which we want to append in file :- ")
file.write(s)
file=open("Temp_file.txt",'a')
file.close()