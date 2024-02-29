# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Method 1: Append - adds an element to the end of the list
numbers.append(6)
print("After append:", numbers)

# Method 2: Insert - inserts an element at a specific index
numbers.insert(2, 10)
print("After insert:", numbers)

# Method 3: Remove - removes the first occurrence of a specific value
numbers.remove(3)
print("After remove:", numbers)

# Method 4: Pop - removes and returns the element at a specific index
popped_element = numbers.pop(1)
print("Popped element:", popped_element)
print("After pop:", numbers)

# Method 5: Index - returns the index of the first occurrence of a value
index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)

# Method 6: Count - returns the number of occurrences of a value
count_of_5 = numbers.count(5)
print("Count of 5:", count_of_5)

# Method 7: Sort - sorts the list in ascending order
numbers.sort()
print("After sort:", numbers)

# Method 8: Reverse - reverses the order of elements in the list
numbers.reverse()
print("After reverse:", numbers)

# Method 9: Len - returns the number of elements in the list
length_of_numbers = len(numbers)
print("Length of numbers:", length_of_numbers)
