# Get input from the user
purchase_amount = float(input("Enter the purchase amount: "))
is_premium_member = input("Are you a premium member? (yes/no): ").lower() == "yes"

# Initialize discount percentage
discount_percentage = 0

# Apply discount based on conditions using logical operators
if purchase_amount > 300 and is_premium_member:
    discount_percentage = 20
elif purchase_amount > 200 or is_premium_member:
    discount_percentage = 10
else:
    discount_percentage = 5

# Calculate the discounted amount
discounted_amount = purchase_amount - (purchase_amount * discount_percentage / 100)

# Display the results
print(f"Original amount: ${purchase_amount}")
print(f"Discount percentage: {discount_percentage}%")
print(f"Discounted amount: ${discounted_amount}")