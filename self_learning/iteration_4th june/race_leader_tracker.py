# Program to find fastest racer, slowest racer,
# and difference between their lap times
# Input number of racers
n = int(input("Enter number of racers: "))

# Input first racer's lap time
time = float(input("Enter lap time of racer 1: "))
fastest = slowest = time
fastest_pos = slowest_pos = 1

# Input remaining racers' lap times
for i in range(2, n + 1):
    time = float(input(f"Enter lap time of racer {i}: "))

    # Check for fastest racer
    if time < fastest:
        fastest = time
        fastest_pos = i

    # Check for slowest racer
    if time > slowest:
        slowest = time
        slowest_pos = i

# Calculate difference
difference = slowest - fastest

# Display results
print("Fastest racer position:", fastest_pos)
print("Slowest racer position:", slowest_pos)
print("Difference in lap times:", difference)
