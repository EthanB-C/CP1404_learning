class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello my name is " + self.name)


p1 = MyClass("John", 36)

print(p1.name)
print(p1.age)
p1.my_function()
