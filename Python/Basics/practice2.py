price1 = float(input("Price 1: "))
price2 = float(input("Price 2: "))
price3 = float(input("Price 3: "))

total_bill = price1 + price2 + price3
average_price = total_bill / 3

print("Total bill amount:", total_bill)
print("Average price:", average_price)

superhero_name = input("Superhero name: ")

if superhero_name.lower().startswith("s"):
    print("The superhero name starts with 'S' or 's'.")
else:
    print("The superhero name does not start with 'S' or 's'.")
