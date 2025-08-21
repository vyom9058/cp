A = int(input("enter a number:"))
before = A
after = 0
while A > 0:
    digit = A % 10           
    after = after * 10 + digit 
    A //= 10                 
if before == after:
    print("Yes")  
else:
    print("No")   