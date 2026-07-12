import random
def rollslot():
    symbols=['🍒','⭐','💰','😂']
    row=[random.choice(symbols) for _ in range(3)]
    return row
def showslot(row):
    print("_________")
    print("|".join(row))
    print("_________")
def getpayoff(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='😂':
            pay=bet*3
        if row[0]=='🍒':
            pay=bet*5
        if row[0]=='⭐':
            pay=bet*10
        if row[0]=='💰':
            pay=bet*20
    else:
        pay=0
    return pay

print("-----------------------")
print("welcome to slot machine")
print("-----------------------")
balance=100
while balance>0:
    print(f"your balance  is: {balance}")
    bet=input("place your bet:")
    if not bet.isdigit():
        print("not a valid input.")
        continue
    bet=int(bet)
    if bet<0:
        print("bet must be greater than 0")
        continue
    if bet>balance:
        print("insufficient balance")
        continue
    
    balance-=bet
    row=rollslot()
    print("spinning...")
    showslot(row)
    pay=getpayoff(row,bet)
    if pay>0:
        print(f"congrats you won ${pay}")
        balance+=pay
    else:
        print("sorry you didn't get anything")
    if input("do you wnat to play again(y/n)").lower() != "y":
        break