l = [1,2,3,"four",5.0,True]
print(l)
print(type(l))

# Accessing elements
print(l[0])    # First element
print(l[3])    # Fourth element
print(l[-1])   # Last element
print(l[-5])   # Second element

# Slicing
print(l[1:4])   # Elements from index 1 to 3
print(l[:3])    # First three elements
print(l[2:])    # Elements from index 2 to end

# Modifying elements
l[3] = "FIVE"
print(l)

# Adding elements
l.append("new item")   # Add to the end
print(l)
l.insert(2, "inserted item")  # Insert at index 2
print(l)

# Removing elements
l.remove(5.0)   # Remove first occurrence of 5.0
print(l)
popped_item = l.pop()  # Remove and return last item
print(popped_item)
print(l)

# Length of the list
print(len(l))