#using dictionaries
print("=====================MENU=======================")
menu={"pizza": 100.25,
      "popcorn": 120.52,
      "sprite": 89.03,
      "fries": 60.40,
      "nachos": 50.87,
      "chips": 65.82 }
cart=[]
total=0
for key,value in menu.items():
    print (f"{key:10}:  {value:.2f}")

while True:
    product=input("enter your item(q to quit): ").lower()
    if product == 'q':
        break
    elif menu.get(product) is not None:
        cart.append(product)
        total+=menu.get(product)
    else:
        print("item is not present in the menu")
print("--------------------------------------------------")
print(f"{'your cart':^50}")
print("--------------------------------------------------")
for c in cart:
    print(f"{c:10}:{menu.get(c):>8.2f}")
print("---------------------")
print(f"your total:{total:>8.2f}")