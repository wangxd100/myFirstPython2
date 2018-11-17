
# create unique elements in the list
# and also sort order for you

testSet = set()
testSet.add(5)
testSet.add(1)
testSet.add(2)
testSet.add(1)
testSet.add("b")
testSet.add("a")
print(testSet)

myList = [1, 3,1, 4,3]
mySet = set(myList)
total = 0
for x in mySet:
    total += x
print(total)

# shortcut
print(sum(mySet))
