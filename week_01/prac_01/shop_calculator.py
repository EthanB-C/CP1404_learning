"""Shop Calculator"""
DISCOUNT_RATE = 0.1
total_cost = 0

number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_items = float(input("Price of item: "))
    total_cost += price_of_items
if total_cost > 100:
    discount = DISCOUNT_RATE * total_cost
    total_cost -= discount
print(f"Total price for {number_of_items} items is ${total_cost:.2f}")
