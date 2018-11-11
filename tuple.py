# list
my_list = ["1", 2, 3, 4, "5"]

# tuple
my_tuple = (1, 0, 3, "4", 5)

print(my_tuple)
print(len(my_list))
print(len(my_tuple))

print(my_list[4])
print(my_tuple[4])

print(type(my_list))
print(type(my_tuple))

# print(dir(my_list))
# print(".....")
# print(dir(my_tuple))

# list is mutable
# tuple is inmutable 不可更改， 功能少， 速度快

my_list.remove(4)
print(my_list)


