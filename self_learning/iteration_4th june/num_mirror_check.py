# Program to check whether a number is a Mirror Number
# A mirror number has identical left and right halves
# Accept the number as input
num = input("Enter a number: ")

# Find the total number of digits
length = len(num)

# Check if the number of digits is even
if length % 2 != 0:
    print("Number must have an even number of digits.")
else:
    # Find the middle position
    mid = length // 2

    # Extract the left half of the number
    left_half = num[:mid]

    # Extract the right half of the number
    right_half = num[mid:]

    # Compare both halves
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
