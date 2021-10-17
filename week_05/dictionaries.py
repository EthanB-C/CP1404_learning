ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}
# new_name = input("Name: ")
# new_age = int(input("Age: "))
# ages_dict[new_name] = new_age
# for name in ages_dict:
#     print("{} - {}".format(name, ages_dict[name]))


# new_ones = {name: age for name, age in ages_dict.items() if age > 18}
# print(new_ones)

new_ones = {}
for name, age in ages_dict.items():
    if age > 18:
        new_ones[name] = age
print(new_ones)
