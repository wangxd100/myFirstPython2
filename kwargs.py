print("-----1st test -----")
def myFunc(*args, **kwargs):
    print("type of args:",type(args))
    print("type of kwargs:", type(kwargs))

myFunc()

dic_1 = {"name":"sheldon", "age":"40", "sex":"male", "height":"180cm"}

for k,v in dic_1.items():
    print(k,":",v)

# 2nd test
print("----- 2nd test -----")
def someone(dic_var):
    for k, v in dic_var.items():
        print(k,"--",v)
someone(dic_1)

# 3rd test
print("-----3rd test ------")
def someone2(**kwargs):
    for k,v in kwargs.items():
        print(k,"::",v)
someone2(name="sheldon wang", age="47 years old")




