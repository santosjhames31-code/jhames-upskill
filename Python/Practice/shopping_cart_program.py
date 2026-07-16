#Shopping Cart Program
#python shopping_cart_program.py

items = []
prices = []
total_price = 0

while True:
    item = input("Enter Item (Enter q to quit) : ")
    if item.upper() == 'Q':
        break
    price = float(input(f"Enter price for {item} : "))
    items.append(item)
    prices.append(price)
    total_price += price

for i in range(len(items)):
    print(f"Item  : {items[i]}")
    print(f"Price :  {prices[i]:.2f} ")
    print()

print(f"Total : $ {total_price:.2f}")

