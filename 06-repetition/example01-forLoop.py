student_number = int(input("Student number : "))

for i in range(student_number):
    score = int(input("Turn in your score : "))
    if score >= 80:
        print("You got grade A")
    elif score >= 75:
        print("You got grade B+")
    elif score >= 70:
        print("You got grade B")
    elif score >= 65:
        print("You got grade C+")
    elif score >= 60:
        print("You got grade C")
    elif score >= 55:
        print("You got grade D+")
    elif score >= 50:
        print("You got grade D")
    else:
        print("You got grade F")

