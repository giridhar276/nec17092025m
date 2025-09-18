

fobj = open("customers.txt","w")

fobj.write("python programming\n")
fobj.write("genai\n")

fobj.writelines(["unix","python","java\n"])

for value in range(1,10):
    fobj.write(str(value)  + "\n")

fobj.close()



fobj = open("customers.txt","a")
fobj.write("machine learning\n")
fobj.close()
