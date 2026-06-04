num = int(input("Enter a number: "))
# Save original number
temp = num

# Store sum of factorials
sum_of_factorials = 0

# Process each digit
while temp > 0:
    digit = temp % 10

    # Find factorial
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    # Add factorial to sum
    sum_of_factorials += factorial

    # Remove last digit
    temp //= 10

# Check Strong Number
if sum_of_factorials == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")
    
