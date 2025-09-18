book = {"chap1":10 ,"chap2":20 ,"chap3":30,"chap1":1000}
print("Initial dictionary :", book)

#adding new key-value
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60

print("Updated book :",book)

# display individual values
print(book['chap1'])
print(book['chap2'])
print(book['chap3'])

# display keys
print(book.keys())
print("keys:")
for key in book.keys():
    print(key)

print("keys:")
for key in book:
    print(key)

# display values
print("values")
print(book.values())

for value in book.values():
    print(value)

# display items
for key,value in book.items():
    print(key,value)