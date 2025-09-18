try:
    fobj = open("employees111.txt","r")
    for line in fobj:
        print(line.strip())
    fobj.close()
except FileNotFoundError as err:
    print(err)
    print("file is not found")

###############################################################

try:
    fobj = open("employees111.txt","r")
    for line in fobj:
        print(line.strip())
    fobj.close()
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
    print("file is not found")