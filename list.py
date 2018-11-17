my_list = ["sheldon", "wang", 47, 627]
# help(my_list)

# print(my_list)
print(my_list[0])
my_list.append("0226")
print(my_list)
print("length: " + str(len(my_list)))

# my_list.remove("wang")
# print(my_list)
# print(my_list.count(47))


def my_func():
    print("my function!")
    print("2nd line.")
    print("3rd line")

my_func()


listPosition = [1, 2, 4, 6, 8]
# 1st position
print(listPosition[0])
# last position
print(listPosition[len(listPosition)-1])
print(listPosition[-1])