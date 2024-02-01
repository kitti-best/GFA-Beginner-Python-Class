# Get chest circumference from user input
chest_circumference = float(input("Enter the chest circumference in inches: "))

# Determine the size based on chest circumference
if chest_circumference < 37:
    size = 'XS'
elif 37 <= chest_circumference < 41:
    size = 'S'
elif 41 <= chest_circumference < 43:
    size = 'M'
elif 43 <= chest_circumference < 46:
    size = 'L'
else:
    size = 'XL'

# Display the determined size
print(f"The size of the polo t-shirt based on chest circumference is: {size}")
