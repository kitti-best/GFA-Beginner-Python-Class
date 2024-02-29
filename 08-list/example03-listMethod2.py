# Initialize an empty to-do list
todo_list = []

# Add tasks to the to-do list
todo_list.append("Complete math homework")
todo_list.append("Buy groceries")
todo_list.append("Read a book")

# Display the to-do list
print("To-Do List:")
print("- " + "\n- ".join(todo_list))

# Mark a task as completed
completed_task = "Buy groceries"
if completed_task in todo_list:
    todo_list.remove(completed_task)
    print(f"\nTask '{completed_task}' completed!")

# Display the updated to-do list
print("\nUpdated To-Do List:")
print("- " + "\n- ".join(todo_list))
