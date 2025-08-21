n = int(input("enter a number:"))
total = 0
i = 1
while i <= n:
    
    if i % 2 != 0:
        total = total + i
    i += 1
print(total)
    