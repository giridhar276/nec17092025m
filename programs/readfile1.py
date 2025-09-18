# displaying line by line
fobj = open("employees.txt","r")
for line in fobj:
    print(line.strip())
fobj.close()

print("---------------------------------------------------")
## using fobj.read() -------> string
fobj = open("employees.txt","r")
print(fobj.read())  # ctrl+a   then ctrl + C    then ctl + P
fobj.close()

print("---------------------------------------------------")
# using fobj.readlines() -----> list
fobj = open("employees.txt","r")
print(fobj.readlines())
fobj.close()