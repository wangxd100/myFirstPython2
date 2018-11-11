import test1

myList = []

for i in range(11):
    myList.append(i*2)
print(myList)

print([j*2 for j in range(11)])

###### 2nd example ############
nameList = ['sheldon', 'wang', 'cindy', 'dong', 'daniel']

emptyList = []
for name in nameList:
    if name.startswith("d"):
        emptyList.append(name)
print("1st:",emptyList)

print("2nd:",[name for name in nameList if name.startswith("d")])


def add1(a,b,c):
    print(a+b+c)
add1(1,2,3)





def add2(*args):
    print(sum(args))
add2(2,3,5)

def printing(*arg):
    for name in arg:
        print("family member: ", name)

printing("sheldon" ,"cindy", "daniel", "Katie")


# call test1.py module
test1.printTest()



