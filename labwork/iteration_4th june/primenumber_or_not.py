# Program to check whether a number is prime or not
# Take input from user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(num, "is not a prime number")

else:
    # flag variable to track prime status
    is_prime = True

    # check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # number is divisible, so not prime
            break  # no need to check further

    # final result
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
