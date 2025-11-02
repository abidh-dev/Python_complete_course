mytup = (10, 20, 30, 40, 50)
print("Original tuple:", mytup)

# Accessing elements
print("First element:", mytup[0])    # First element
print("Fourth element:", mytup[3])    # Fourth element

# Slicing
print("Elements from index 1 to 3:", mytup[1:4])   # Elements from index 1 to 3
print("First three elements:", mytup[:3])    # First three elements
print("Elements from index 2 to end:", mytup[2:])    # Elements from index 2 to end

# Tuples are immutable, so the following line would raise an error if uncommented
#mytup[2] = 100  # This will raise a TypeError

# methods
print("Count of 20 in tuple:", mytup.count(20))  # Count
print("Index of 30 in tuple:", mytup.index(30))  # Index