"""Demo showing two programs: without and with CONSTANTS."""
print("If you buy over 5 items, save 10%!")
number_of_products = int(input("Number of products: "))
while number_of_products < 1:
    print("Invalid number")
    number_of_products = int(input("Number of products: "))
total = number_of_products * 32.5
if number_of_products > 5:
    total -= total * 0.1
print(f"{number_of_products} x ${32.5:.2f} products = ${total:.2f}")

# version 2 - notice how it is easier to read,
# and now we only have one place to change if we need to update the values
DISCOUNT_THRESHOLD = 5
ITEM_PRICE = 32.5
DISCOUNT_RATE = 0.1

print(f"If you buy over {DISCOUNT_THRESHOLD} items, save {DISCOUNT_RATE * 100:.0f}%!")
number_of_products = int(input("Number of products: "))
while number_of_products < 1:
    print("Invalid number")
    number_of_products = int(input("Number of products: "))
total = number_of_products * ITEM_PRICE
if number_of_products > DISCOUNT_THRESHOLD:
    total -= total * DISCOUNT_RATE
print(f"{number_of_products} x ${ITEM_PRICE:.2f} products = ${total:.2f}")
