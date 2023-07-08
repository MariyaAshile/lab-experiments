Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125},
}

# Display the current grocery items
print("Item details before updating:")
for item, details in Grocery.items():
    quantity = details["quantity"]
    price = details["price"]
    print(f"{item}: Quantity - {quantity} kg, Price - {price} Rs")

# User input
choice = int(input("Enter your choice (1. Add quantity, 2. Update price, 3. Add new item): "))
if choice == 1:
    item_name = input("Enter the grocery item name: ")
    quantity_added = int(input("Enter the quantity of the item to be added: "))

    if item_name in Grocery:
        Grocery[item_name]["quantity"] += quantity_added
        print("Quantity updated successfully!")
    else:
        print("Item not found in the grocery list.")

# Display the updated grocery items
print("\nItem details after updating:")
for item, details in Grocery.items():
    quantity = details["quantity"]
    price = details["price"]
    print(f"{item}: Quantity - {quantity} kg, Price - {price} Rs")
