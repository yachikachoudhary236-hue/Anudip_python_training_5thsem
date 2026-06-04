# Program to find the minimum number of notes required
# Available denominations: 500, 200, 100, 50, 20, 10

# Accept the amount from the user
amount = int(input("Enter the amount: "))

# List of available note denominations in descending order
notes = [500, 200, 100, 50, 20, 10]

# Variable to store the total number of notes used
total_notes = 0

print("Notes required:")

# Process each denomination
for note in notes:
    # Find how many notes of the current denomination are needed
    count = amount // note

    # If at least one note is needed, display it
    if count > 0:
        print(note, "x", count)

        # Add the count to the total number of notes
        total_notes += count

        # Update the remaining amount
        amount = amount % note

# Display the minimum number of notes used
print("Total number of notes =", total_notes)
