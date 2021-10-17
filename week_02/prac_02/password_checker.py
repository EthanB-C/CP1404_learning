"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
MIN_UPPER_CHAR = 1
MIN_LOWER_CHAR = 1
MIN_NUMBER_CHAR = 1
MIN_SPECIAL_CHAR = 1
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print(f"\t{MIN_UPPER_CHAR} or more uppercase characters")
    print(f"\t{MIN_LOWER_CHAR} or more lowercase characters")
    print(f"\t{MIN_NUMBER_CHAR} or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand {MIN_SPECIAL_CHAR} or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    else:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            count_lower += char.islower()
            count_upper += char.isupper()
            count_digit += char.isnumeric()
        if count_lower < MIN_LOWER_CHAR or count_upper < MIN_UPPER_CHAR or count_digit < MIN_NUMBER_CHAR:
            return False
        if SPECIAL_CHARS_REQUIRED:
            for char in password:
                count_special += char in SPECIAL_CHARACTERS
            if count_special < MIN_SPECIAL_CHAR:
                return False
        return True


main()
