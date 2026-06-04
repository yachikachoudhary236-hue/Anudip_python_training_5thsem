 #Program: Electricity Bill Calculator
# Take input from user
units = float(input("Enter number of units consumed: "))

# Initialize bill amount
bill = 0

# Slab 1: 0 - 100 units (Rs. 5 per unit)
if units <= 100:
    bill = units * 5

# Slab 2: 101 - 200 units (Rs. 7 per unit)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

# Slab 3: Above 200 units (Rs. 10 per unit)
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Display final bill
print("Electricity Bill = Rs.", bill)
