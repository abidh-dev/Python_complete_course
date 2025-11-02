num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
elif num % 2 != 0:
    print(f"{num} is odd.")
else:
    print("Invalid input.")