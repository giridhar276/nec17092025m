
with open("employees.txt","r") as fobj:
    deparmentlist =  []
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        print(output[1].upper())
        deparmentlist.append(output[2])
    
    print("all available departments")
    for item in deparmentlist:
        print(item.lower())
    