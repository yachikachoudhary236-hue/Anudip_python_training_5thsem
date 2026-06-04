# Program: Display battery charging level

charging_level = 20          # Initial battery percentage
electricity_status = True    # (Not used in this program)

# Loop runs until battery reaches 100%
while (charging_level <= 100):

    # This condition is always True because charging_level is a number
    if (charging_level):

        # Display current battery level
        print("Battery charging level:", charging_level, "%")

        # Increase battery charging level by 10%
        charging_level += 10

    else:
        # This part will never execute in current logic
        break

# When loop ends, battery is full
print("Full charge")
