age = int(input("Enter your age: "))
is_citizen = input("Are you a citizen? (yes/no): ").lower() == "yes"

# Check eligibility using logical operators
if age >= 18 and is_citizen:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")