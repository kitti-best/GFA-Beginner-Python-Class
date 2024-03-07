import random
from random import randint

my_list = []

while len(my_list) < 10:
    my_list.append(randint(1, 10))

my_list.sort()

ans = []

print("Initial list :", my_list)
for item in my_list:
    if item not in ans:
        ans.append(item)

print("Result list :", ans)
print()
