# Input the integer
n1 = int(input("Enter the number: "))

# Check if the number is 0 first
if n1 == 0:
    print("0 is neither odd nor even")

# Finding the remainder to check for even or odd
elif n1 % 2 == 0:
    print(f"The number {n1} is even")

# If it's not even, it's odd
else:
    print(f"The number {n1} is odd")
