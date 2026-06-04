# Program to check whether a number contains consecutive digits
# Input number from the user
num = int(input("Enter a number: "))

# Convert number to string for easy digit access
num_str = str(num)

# Assume digits are consecutive initially
is_consecutive = True

# Check each pair of adjacent digits
for i in range(len(num_str) - 1):
    # If the next digit is not 1 greater than the current digit
    if int(num_str[i + 1]) != int(num_str[i]) + 1:
        is_consecutive = False
        break

# Display result
if is_consecutive:
    print("The number has consecutive digits.")
else:
    print("The number does not have consecutive digits.")
