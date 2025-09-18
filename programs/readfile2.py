# displaying line by line
fobj = open("employees.txt","r")
for line in fobj:
    print(line.strip())
fobj.close()

# context manager
# if any line starts using 'with' keyword .. it is context manager
# file is opened inside the context
# Advantage: file gets clsoed automatically
with open("employees.txt","r") as fobj:
    print(fobj.read())

####################################################################
fobj = open("customers.txt","w")
fobj.write("python programming\n")
fobj.write("genai\n")
fobj.close()

### using context manager
with open("customers.txt","w") as fobj:
    fobj.write("python programming\n")
    fobj.write("genai\n")

