# Program to check Armstrong number
# Take input from user
num = int(input("Enter a number: "))

# Store original number for final comparison
original_num = num

# Find number of digits
digits = len(str(num))

# Variable to store sum of digits raised to power
sum_of_powers = 0

# Loop through each digit of the number
while num > 0:
    digit = num % 10              # extract last digit
    sum_of_powers += digit ** digits  # raise digit to power of total digits
    num = num // 10               # remove last digit

# Check if original number is equal to calculated sum
if sum_of_powers == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")
