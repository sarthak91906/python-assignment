print("Vendor Details")

name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

total = 0

print("\nEnter Monthly Purchase Amount:")
for i in range(1, 13):
    amount = float(input("Month " + str(i) + ": "))
    total = total + amount

average = total / 12

print("\n--- Annual Purchase Report ---")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", total)
print("Average Monthly Purchase:", average)