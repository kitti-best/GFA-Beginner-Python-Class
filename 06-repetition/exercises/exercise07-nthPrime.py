needed_prime = int(input("How many prime number you want : "))
count = 0
n = 2

while count < needed_prime: 
    prime = True
    if n < 2:
        prime = False
    
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0 or not prime:
            prime = False
            break
    if prime:
        print(f"{count + 1}. Number {n} is Prime")
        count += 1
    n += 1

