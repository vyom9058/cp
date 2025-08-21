n = int(input("enter a number:"))
digit = 0
while n > 0:
    n = n // 10
    digit = digit + 1
print(digit)    