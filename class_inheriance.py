class Father:
    name = "Sheldon"

    def walk(self):
        print("father can walk")


class Mother:
    def eat(self):
        print("mother can eat")


class Son(Father, Mother):
    pass
    def eat(self):
        print("son can eat, too")

    def walk(self):
        print("son can walk, too")


child = Son()
child.walk()
child.eat()


