student_list = []
n = int(input("Number of student : "))

for i in range(n):
    student_info = {}
    name = input("Student name : ")
    score = int(input("Student score : "))
    age = int(input("Student age : "))

    student_info["age"] = age
    student_info["name"] = name
    student_info["score"] = score
    
    print()
    
    student_list.append(student_info)

