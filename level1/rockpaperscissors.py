import random

choices=("rock","paper", "scissor")
flag=True
while flag:
    person=None
    while person not in choices:
        person=input("enter your choice: (rock,paper,scissor)")
    
    computer=random.choice(choices)
    print("your choice: ",person)
    print("computer choice:", computer)
    if person=="rock" and computer=="scissor":
        print("you win")
    elif person=="scissor" and computer=="paper":
        print("you win")
    elif person=="paper" and computer=="rock":
        print("you win")
    elif person==computer:
        print("its a tie")
    else:
        print("you loose")
    if input("do you want to play again(y/n)").lower()=="n":
        flag=False
