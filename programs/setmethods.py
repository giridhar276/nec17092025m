

aset = {10,10,20,20,20,30,30}
print(aset)

bset = {30,30,30,40,40,50,50}
print(bset)

aset.add(10)
print("after updating:",aset)
aset.add(40)
print("after updating:",aset)


print(aset.union(bset))
print(aset.intersection(bset))
print(aset.difference(bset))
print(aset.issubset(bset))
print(aset.issuperset(bset))