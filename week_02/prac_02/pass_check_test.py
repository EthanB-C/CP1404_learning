# count_lower = 0
# password = 'maxerKKK'
# for char in password:
#     count_lower += char.islower()
# print(count_lower)
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
count_special = 0
password = 'cop!!!'
for char in password:
    count_special += char in SPECIAL_CHARACTERS
print(count_special)
