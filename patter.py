n = int(input("enter a number:"))
m = int(input("enter a number:"))
for i in range(1,n+1):
  for j in range(n+1-i):
   print("*", end=" ")
  print() 