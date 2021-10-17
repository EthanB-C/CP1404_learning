"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= BONUS_THRESHOLD:
        bonus_percentage = 0.15
    else:
        bonus_percentage = 0.10
    bonus = sales * bonus_percentage
    print(f"Your bonus is ${bonus}.")
    sales = float(input("Enter sales: $"))
print("Done")
