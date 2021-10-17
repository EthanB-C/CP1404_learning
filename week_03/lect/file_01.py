try:
    age = int(input("What is your age? "))
    while age < 0:
        print("invalid age")
        age = int(input("What is your age? "))
    else:
        if age % 2 == 1:
            print("Odd")
        else:
            print("Even")
except ValueError:
    print("invalid age")
    age = int(input("What is your age? "))
