#wap to analyze prime number ,accept a number from user and check whether it is prime or not.and print factor if it is not a prime number. 
num = int(input("enter a number"))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not a prime number")
            print("Factors of", num, "are:", end=" ")
            for j in range(1, num + 1):
                if num % j == 0:
                    print(j, end=" ")
            print()
            break
    else:       
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")
