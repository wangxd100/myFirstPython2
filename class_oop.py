# Object Oriented Program
class Student():
    def eat(self):
        print("student can eat!")

    def study(self):
        print("must work smart!")
Student().eat()
boy = Student()

Student().eat()
boy.eat()
boy.study()

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






