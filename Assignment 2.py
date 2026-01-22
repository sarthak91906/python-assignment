# Lab Assignment 2
# Vendor Annual Purchase Report

# Vendor details
vendor_name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly_purchases = []
total_purchase = 0

print("\nEnter Monthly Purchase Amounts:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    monthly_purchases.append(amount)
    total_purchase += amount

# Output
print("\n------ Vendor Annual Billing Report ------")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Monthly Purchases:", monthly_purchases)
print("Total Annual Purchase:", total_purchase)
