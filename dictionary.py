# dictionary
myDictionary ={"key1" : "value", "key2" : "value2"}
print(myDictionary)
print(myDictionary["key2"])

myDictionary["key2"] = "value2z222"

print(myDictionary)

age = input("please enter your age:")
print(type(age))

if int(age) < 21:
    print("too young!")
elif int(age) >= 21 and int(age) <75:
    print("audlt !")
elif int(age) >= 75:
    print("old man")


print("done!")

