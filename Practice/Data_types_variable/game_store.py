
print("Welcome to the Game store!")

game = int(input("Press 1 to buy God of War, Price is 17.69\n"
             "Press 2 to buy Mario, Price is 25.79\n"
             "Press 3 to buy Sonic, Price is 21.64\n"
             "Press 4 to buy Asteroid, Price is 12.89:\n"))

amount = float(input("Enter the amount: "))

if game == 1:
    print("You have purchased God of War!")
    price = 17.69
    tax = price*0.08
    total = price + tax
    print(f"Price of game: {price}\nTax @8%: {tax}\nTotal: {total}")
    print(f"Changed amount is: {amount-total}")
elif game == 2:
    print("You have purchased Mario!")
    price = 25.79
    tax = price*0.08
    total = price + tax
    print(f"Price of game: {price}\nTax @8%: {tax}\nTotal: {total}")
    print(f"Changed amount is: {amount-total}")
elif game == 3:
    print("You have purchase Sonic!")
    price = 21.64
    tax = price*0.08
    total = price + tax
    print(f"Price of game: {price}\nTax @8%: {tax}\nTotal: {total}")
    print(f"Changed amount is: {amount-total}")
elif game == 4:
    print("You have purchase Asteroid!")
    price = 12.89
    tax = price*0.08
    total = price + tax
    print(f"Price of game: {price}\nTax @8%: {tax}\nTotal: {total}")
    print(f"Changed amount is: {amount-total}")
else:
    print("Invalid input game not available.")