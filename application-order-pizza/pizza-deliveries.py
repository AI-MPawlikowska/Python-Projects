print("Welcome to PYTHON Pizza deliveries!")


size = input("What size pizza do you want? S, M, or L:\n").upper()
price = 0

if size == "S":
    price = 15
    print("Small pizza costs $15.")
elif size == "M":
    price = 20
    print("Medium pizza costs $20.")
elif size == "L":
    price = 25
    print("Large pizza costs $25.")
else:
    print("Invalid size. Please choose S, M, or L.")
    exit()


extra_cost = 0

pepperoni = input("Do you want pepperoni on your pizza? y or n: ").lower()
if pepperoni == "y":
    extra_cost += 5
    print(f"Pepperoni costs $5.")

extra_cheese = input("Do you want extra cheese? y or n: ").lower()
if extra_cheese == "y":
    extra_cost += 2
    print(f"Extra cheese costs $2.")


total_cost = price + extra_cost
print(f"Your total cost is: ${total_cost}. Thank you for your order!")


