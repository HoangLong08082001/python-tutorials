# List 
emptyList = []

emptyList2 = list()
print(emptyList)
print(emptyList2)

# Create List with values
colors = ['green','red','yellow']
print(colors)

students = ['John', 'Jane', 'Jack', 'Jill']
print(students[1])

# Add new item to the end of a list
students.append('Tom')
print(students) 

# Remove an item from a list by value
students.remove('Tom')
print(students)

# Insert an item at specific index
students.insert(1,'Ha')
print(students)

# Remove an item if it exists
if 'Jane' in students: 
    students.remove('Jane')
    print(students)

# Remove an item at specific index
students.pop(1)
print(students)

# Get length of a list
print(len(students))

# Reverse items in a li
students.reverse()
print(students)

# Sort items in a li
students.sort() # reverse=True for descending order
print(students)

# Clear all items in a li
students.clear()
print(students)