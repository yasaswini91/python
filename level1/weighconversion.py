w=float(input("enter the weight: "))
x=input("kgs or pounds(K/L): ")

if x == "K":
    w*=2.205
    x="lbs."
    print(f"your converted weight is {round(w,1)} {x}")
elif x == "L" :
    w/=2.205
    x="kgs"
    print(f"your converted weight is {round(w,1)} {x}")
else:
    print("enter valid weights")