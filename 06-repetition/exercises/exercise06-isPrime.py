n = int(input("The number : "))

prime = True
if n < 2:
    prime = False

for i in range(2, int(n**(0.5)) + 1):
    if n % i == 0 or not prime:
        prime = False
        break

print(f"Number {n} is " + "Not " * int(not prime) + "Prime")
