
# __init__ class

class Students:
    def __init__(self, name, age):
        self.name = name
        self.ages = age

    def walk(self):
        print(self.name, "can walk")
        print(self.name, "is", self.ages)

s1 = Students("sheldon", 40)
s1.walk()

s2 = Students("Daniel", 17)
s2.walk()