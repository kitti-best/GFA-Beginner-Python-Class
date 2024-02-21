import math

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    area = math.pi * radius**2
    return area

def calculate_circle_diameter(radius):
    """Calculate the diameter of a circle."""
    diameter = 2 * math.pi * radius
    return diameter

# Example usage:
radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)
diameter = calculate_circle_diameter(radius)

print(f"Area of the circle: {area}")
print(f"Diameter of the circle: {diameter}")
