# Program: Attendance Counter

# Take number of students as input
student = int(input("Enter the number of students in the class: "))

# Initialize attendance counter
attendance = 0

# Check for invalid input (negative number of students)
if student < 0:
    exit("Invalid input. Number of students cannot be negative.")

# NOTE: The following lines are incorrectly placed in your code
# They will NOT run because program exits above for invalid input

students = 0   # (This variable is not needed / not used correctly)
print(students)

# Loop to count attendance
while (attendance <= student):

    # This condition is always True if attendance != 0
    if (attendance):

        # Print current attendance count
        print("Attendance count:", attendance)

        # Increase attendance by 1
        attendance += 1

    else:
        # This part runs only when attendance = 0
        break
