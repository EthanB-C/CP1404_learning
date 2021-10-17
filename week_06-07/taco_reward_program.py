"""Taco Reward Program"""


class User:
    def __init__(self, name, score):
        self.number_of_tacos = 5
        self.name = name
        self.score = score

    def give_user_tacos(self, user):
        self.number_of_tacos -= 1
        user.number_of_tacos += 1
        self.score += 5


Jack = User('Jack', 5)
Max = User('Max', 10)
print(f"{Jack.name} has {Jack.score} points and {Jack.number_of_tacos} tacos left")
print(f"{Max.name} has {Max.score} points and {Max.number_of_tacos} tacos left")
Jack.give_user_tacos(Max)
print(f"{Jack.name} has {Jack.score} points and {Jack.number_of_tacos} tacos left")
print(f"{Max.name} has {Max.score} points and {Max.number_of_tacos} tacos left")
