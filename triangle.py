a = int(input("enter first angle:"))
b = int(input("enter second angle:"))
c = int(input("enter third angle:"))

if a+b+c == 180 and a > 0 and b > 0 and c > 0:
    if a == 90 or b == 90 or c == 90:
        print("it is a right angle triangle")
    elif a > 90 or b > 90 or c > 90:
        print("it is a obtuse angle triangle")
    else:
        print("it is a acute angle triangle")
else:
    print("angles are not correct")                