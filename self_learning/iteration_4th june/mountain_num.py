# Program to check whether a number is a Mountain Number

# Input number from the user
num = input("Enter a number: ")

# Convert each digit into an integer and store in a list
digits = [int(d) for d in num]

# Find the peak (highest digit position)
peak = digits.index(max(digits))

# A mountain number must have digits on both sides of the peak
if peak == 0 or peak == len(digits) - 1:
    print("Not a Mountain Number")
else:
    is_mountain = True

    # Check increasing part
    for i in range(peak):
        if digits[i] >= digits[i + 1]:
            is_mountain = False
            break

    # Check decreasing part
    if is_mountain:
        for i in range(peak, len(digits) - 1):
            if digits[i] <= digits[i + 1]:
                is_mountain = False
                break

    # Display result
    if is_mountain:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")
