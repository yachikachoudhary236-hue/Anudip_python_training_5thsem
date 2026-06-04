# Program to calculate electricity bill using slab rates
# Input units consumed
units = int(input("Enter the number of units consumed: "))

# Calculate bill according to slabs
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Add 10% surcharge if bill exceeds Rs. 5000
if bill > 5000:
    surcharge = bill * 0.10
    bill += surcharge

# Display final payable amount
print("Final Payable Amount = Rs.", bill)
