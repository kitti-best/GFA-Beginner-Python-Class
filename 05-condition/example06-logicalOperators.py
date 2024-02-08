number = int(input("Your number : "))

if number % 4 == 0 and number % 3 == 0:
    print("This number is divisible by both 3 and 4")
    print(number * 2 + 4)
else:
    print("This number is not divisible by both 3 and 4")
    print(number * 2 + 7)
