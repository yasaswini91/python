#inverted right angled triangle
n=int(input("enter size: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()