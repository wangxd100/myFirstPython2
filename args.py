
# arg is tuple type

print("arg is tuple type")

def add1(a, b, c):
    print(a + b + c)

add1(1, 2, 3)


def add2(*args):
    print(sum(args))

add2(2, 3, 5, 45, 6, 5)


def printing(*arg):
    print(type(arg))
    for name in arg:
        print("family member: ", name)


printing("sheldon", "cindy", "daniel", "Katie")
