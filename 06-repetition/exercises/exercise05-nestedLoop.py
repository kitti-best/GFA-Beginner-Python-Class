# # solution 1
# n = int(input("Board size : "))

# for y in range(n):
#     for x in range(n//2 + 1):
#         if y % 2 == 1 and x == 0:
#             print(" ", end="")
#         print("X ", end="")
#     print("")
        
# # solution 2
# n = int(input("Board size : "))

# for y in range(n):
#     for x in range(n):
#         if y % 2 == 1 and x == 0:
#             print(" ", end="")
#         if x % 2 == 0:
#             print("X", end="")
#         else:
#             print(" ", end="")
#     print("")
        
# # solution 3
# n = int(input("Board size : "))

# for y in range(n):
#     for x in range(n):
#         if y % 2 == 1 and x == 0:
#             print(" ", end="")
#         if x % 2 == 0:
#             print("X", end="")
#         else:
#             print(" ", end="")
#     print("")
