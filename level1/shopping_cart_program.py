#shoping cart program using lists

item = []
price=[]
total=0
while True:
    
    it=input("enter your food item(press q to quit): ")
    if it.lower() == 'q':
        break
    else:
        pr=float(input("enter the price of the item: "))
        item.append(it)
        price.append(pr)

print("=============your cart is================")
print(f"{'NO.':<5}  {'item':^15}  {'price':^10}")
for i in range(len(item)):
    
    print (f"{i+1:>3}\t{item[i]:<15}{price[i]:>10.2f}")
    total+=price[i]
print("__________________________________________")
print(f"your total is: $ {total:.2f}")