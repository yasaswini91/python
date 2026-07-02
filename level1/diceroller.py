import random

#● ┌ ─ ┐ │ └ ┘
"┌──────────┐"
"│          │"
"│   ● ● ●  │"
"│          │"
"└──────────┘"

dice_art={
    1:("┌──────────┐","│          │","│    ●     │","│          │","└──────────┘"),
    2:("┌──────────┐","│          │","│   ●  ●   │","│          │","└──────────┘"),
    3:("┌──────────┐","│          │","│   ● ● ●  │","│          │","└──────────┘"),
    4:("┌──────────┐","│   ●  ●   │","│          │","│   ●  ●   │","└──────────┘"),
    5:("┌──────────┐","│   ●  ●   │","│     ●    │","│   ●  ●   │","└──────────┘"),
    6:("┌──────────┐","│   ●  ●   │","│   ●  ●   │","│   ●  ●   │","└──────────┘")
}
dice=[]
total=0
numdice=int(input("enter the number of dice"))
for die in range(numdice):
    dice.append(random.randint(1,6))

'''for i in range(5):
    for die in dice_art:
        if die in dice:
            print(dice_art[die][i],end="   ")
    print("")'''
for i in range(5):
    for die in dice:
        print(dice_art.get(die)[i], end="   ")
    print("")

for die in dice:
    total+=die
print(total)