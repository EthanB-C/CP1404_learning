import random

print(random.randint(5, 20))  # Smallest 5, Largest 20, integer
print(random.randrange(3, 10, 2))  # Smallest 3, Largest 9, integer
print(random.uniform(2.5, 5.5))  # Smallest 2.5, Largest 5.5, float

number = (random.randint(1, 100))
while number != 100:
    print(number)
    number = (random.randint(1, 100))
print(number)
