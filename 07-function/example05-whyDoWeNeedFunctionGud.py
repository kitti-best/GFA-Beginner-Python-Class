import math

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * radius**2

# Function to calculate the volume of a cube
def calculate_cube_volume(side_length):
    return side_length**3

# Main program
while True:
    print("Choose a shape to calculate area or type 'exit' to end:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Cube")

    choice = input("Enter your choice: ")

    if choice.lower() == 'exit':
        break

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"Area of the rectangle: {area}")

    elif choice == '2':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"Area of the circle: {area}")

    elif choice == '3':
        side_length = float(input("Enter the side length of the cube: "))
        volume = calculate_cube_volume(side_length)
        print(f"Volume of the cube: {volume}")

    else:
        print("Invalid choice. Please choose a valid option.")
