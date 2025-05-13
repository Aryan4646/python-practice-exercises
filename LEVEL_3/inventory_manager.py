# Inventory Manager:
# Buy items (decrease stock)
# Restock
# Prevent negative stock

inventory = {"apple": 10, "banana": 15, "kiwi": 12}

print("Press 1 for customer.\nPress 2 for shipment.")
operation = int(input("\nEnter the number: "))

if operation == 1:
    buy = int(input("How many items customer want to buy: "))
    for i in range(buy):
        key = input("Enter the product name customer want to buy: ").casefold()
        value = int(input(f"Quantity of {key}: "))
        if (key in inventory) and (inventory[key] >= value):
            print(f"Succesful Transaction\nYou Purchased {key} with {value} quantity")
            inventory[key] = inventory.get(key) - value
            print(f"New inventory is:\n {inventory}")
        elif (key in inventory) and (inventory[key] < value):
            print(f"Sorry for inconvenience only {inventory[key]} items are left.")
        else:
            print(f"Sorry for inconvenience No such product\nChoose from these items :{inventory}")
if operation == 2:
    item = input("What item came in shipment: ")
    value = int(input("Total number of items: "))
    if item in inventory:
        inventory[item] = inventory.get(item) + value
    else:
        inventory[item] = value
    print(f"New inventory is:\n {inventory}")

