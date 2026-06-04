#wap for strong num verification
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum += factorial
    temp //= 10
if num == sum:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")

    
