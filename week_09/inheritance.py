class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    # def __init__(self, name, age, student_id):
    #     Person.__init__(self, name, age)
    #     self.student_id = student_id
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Musician(Person):
    def play(self):
        text = input("What shall the musician play? ")
        print(text)


mike = Person("Mike", 34)
steve = Musician("Steve", 20)
print(steve.name)
steve.play()
max = Student("Max", 12, 1234)
print(max.student_id)
