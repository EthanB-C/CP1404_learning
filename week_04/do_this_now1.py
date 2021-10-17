name = input("Name: ")
number_of_vowels = 0

for letter in name:
    if letter.lower() in "aeiou":
        number_of_vowels += 1
print("Out of {} letters, {} has {} vowels".format(len(name), name, number_of_vowels))
