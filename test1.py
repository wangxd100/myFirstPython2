######## test from file ifNameEqMain.py #########

test = "name"

print(test * 4)


def printTest():
    print("i am from test1.py file!!!!")


# only execute from this file
# not from Been Imported Class ec. ifNameEqMain.py
if __name__ == '__main__':
    printTest()

# printTest()
