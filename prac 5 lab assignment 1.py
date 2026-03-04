

# Taking input from user
numbers = input("Enter a series of integers separated by space: ")

# Converting input string into tuple of integers
num_list = list(map(int, numbers.split()))
num_tuple = tuple(num_list)

print("\nTuple:", num_tuple)

# a) Total number of items
print("Total number of items:", len(num_tuple))

# b) Last item in tuple
print("Last item in the tuple:", num_tuple[-1])

# c) Tuple elements in reverse order
print("Tuple in reverse order:", num_tuple[::-1])

# d) Check if 5 is present
if 5 in num_tuple:
    print("Yes, 5 is present in the tuple.")
else:
    print("No, 5 is not present in the tuple.")

# e) Remove first and last items, sort remaining
if len(num_tuple) > 2:
    new_tuple = tuple(sorted(num_tuple[1:-1]))
    print("After removing first and last items and sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last.")