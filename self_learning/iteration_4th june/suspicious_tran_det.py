# Program to detect suspicious transactions

# Initialize counters and total amount
above_50000 = 0
below_1000 = 0
total_amount = 0

while True:
    # Accept transaction amount
    amount = int(input("Enter transaction amount (-1 to stop): "))

    # Stop if -1 is entered
    if amount == -1:
        break

    # Add to total transaction amount
    total_amount += amount

    # Count transactions above ₹50,000
    if amount > 50000:
        above_50000 += 1

    # Count transactions below ₹1,000
    if amount < 1000:
        below_1000 += 1

# Display results
print("\nTransactions above ₹50,000 =", above_50000)
print("Transactions below ₹1,000 =", below_1000)
print("Total transaction amount = ₹", total_amount)
