# Object Oriented Program
class Student():
    def eat(self):
        print("student can eat!")

    def study(self):
        print("must work smart!")

    def test(self):
        print("my name is",self.name,"and i like",self.color)
Student().eat()
boy = Student()

boy.eat()
boy.study()
boy.name = "sheldon"
boy.color = "blue"
boy.test()




fruit = "apple"
print(fruit.upper())


class Class():
    course = "it"
    credit="1.0"
    def select(self, course, credit):
        print("i selected",course,"credit is",credit)
        print("self selected", self.course,"credit is",self.credit)

    @staticmethod
    def drop():
        print("i drop class")


Class().select("VR", "0.5")
Class().drop()






