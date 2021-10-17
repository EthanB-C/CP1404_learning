""" files 1."""
OUT_FILE = open('name.txt', 'w')
name = input("Name: ")
print(name, file=OUT_FILE)
OUT_FILE.close()

"""2."""
IN_FILE = open('name.txt', 'r')
print(f"Your name is {IN_FILE.read()}")
IN_FILE.close()

"""3."""
OUT_FILE = open('numbers.txt', 'w')
print('17\n42\n400', file=OUT_FILE)
OUT_FILE.close()

IN_FILE = open('numbers.txt', 'r')
numbers = (IN_FILE.read().split('\n'))
print((int(numbers[0]) + int(numbers[1])))
IN_FILE.close()

"""4."""
IN_FILE = open('numbers.txt', 'r')
total = 0
for line_str in IN_FILE:
    new_str = ''
    line_str = line_str.strip()
    total += int(line_str)
print(total)
IN_FILE.close()
