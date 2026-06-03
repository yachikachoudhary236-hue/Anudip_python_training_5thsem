#wap to calculate simple interest (validate data)
p = float(input( "enter priniciple amount"))
if (p<=0):
    exit("prrinciple amout cannot be negative ")

r = float(input("enter rate"))
if (r<=0):
    exit("rate cannot be negative ")
t = float(input("enter time"))
if (t<=0):
    exit("time cannot be negative ")
else:
   
    print("simple intrest is: ",(p*t*r)/100)
