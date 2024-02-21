def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

for i in range(5):
    num = int(input("Number to find factorial : "))
    print(f"Factorial of {num} is", factorial(num))
