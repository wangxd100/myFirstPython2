import test1

myList = []

for i in range(11):
    myList.append(i * 2)
print(myList)

print("----------list 2-----------")
myList2 = [j * 2 for j in range(11)]
print(myList2)

print("######### 3nd example ##########")
nameList = ['sheldon', 'wang', 'cindy', 'dong', 'daniel']

emptyList = []
for name in nameList:
    if name.startswith("d"):
        emptyList.append(name)

print("1st:", emptyList)

print("2nd:", [name for name in nameList if name.startswith("d")])

