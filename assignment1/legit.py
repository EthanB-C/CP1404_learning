success = False
while success is False:
    try:
        int(input("Is number? "))
        success = True
    except ValueError:
        print("nope")
print("yay")
