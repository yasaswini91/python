que=("how many elements are there in the periodic table",
     "which animal lays largest eggs",
     "what is the hottest planet")
options=(("A.118","B.200","C.119","D.110"),("A.whale","B.ostrich","C.crocodile"),("A.mercury","B.venus","C.jupiter"))
answers=["A","B","B"]
guess=[]
que_num=0
marks=0
for q in que:
    print(q)
    for o in options[que_num]:
        print(o)
    g=input("enter your answer: ")
    guess.append(g.upper())
    if guess[que_num]==answers[que_num]:
        print("CORRECT!")
        marks+=1
    else:
        print(f"INCORRECT, THE ANSWER IS {answers[que_num]}")
    que_num+=1
    print("-----------------------------------------------------------")
print("-------------------------------------------------------------")
print("                         RESULTS                             ")
print("-------------------------------------------------------------")
print(f"answers: {answers}")
print(f"your guess: {guess}")
print(f"YOUR TOTAL IS: {marks}")
score=(marks/len(que))*100
print(f"your percentage is {score:.2f}%")
