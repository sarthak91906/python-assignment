

# Taking input from user
prices = input("Enter prices of sold items separated by space: ")

# Converting input to tuple of floats
price_list = list(map(float, prices.split()))
price_tuple = tuple(price_list)

print("\nPrice Tuple:", price_tuple)

# a) Total number of items sold
print("Total number of items sold:", len(price_tuple))

# b) Price of cheapest item
print("Cheapest item price:", min(price_tuple))

# c) Price of costliest item
print("Costliest item price:", max(price_tuple))

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(price_tuple)))

# e) Number of costliest items sold
costliest_price = max(price_tuple)
count_costliest = price_tuple.count(costliest_price)
print("Number of costliest items sold:", count_costliest)