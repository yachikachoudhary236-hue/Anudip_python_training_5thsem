# Program to find the length of the longest continuous increasing sequence
# Accept the number of elements
n = int(input("Enter the number of elements: "))

# Read the first number
prev = int(input("Enter number 1: "))

# Current increasing sequence length
current_length = 1

# Longest increasing sequence length found so far
max_length = 1

# Read remaining numbers one by one
for i in range(2, n + 1):
    num = int(input(f"Enter number {i}: "))

    # Check if the current number is greater than the previous number
    if num > prev:
        current_length += 1
    else:
        current_length = 1

    # Update maximum length if needed
    if current_length > max_length:
        max_length = current_length

    # Update previous number
    prev = num

# Display the result
print("Length of the longest continuous increasing sequence:", max_length)
