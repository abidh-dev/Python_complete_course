age = int(input("Enter your age: "))

# Determine the life stage based on age
if age >= 18:
    print("You are an adult.")
elif age < 18 and age > 0:
    print("You are a minor.")
elif age == 0 or age < 0:
    print("Invalid age entered.")