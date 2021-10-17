name = "Bobby McAardvark"

count = 0
for letter in name:
    if letter.lower() in 'aeiou':
        count += 1

capitals = [letter for letter in name if letter.isupper()]
new_name = [c for c in name if c.lower() not in "aeiou"]
for letter in new_name:
    print(letter, end="")
