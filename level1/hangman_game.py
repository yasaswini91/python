import random
words=("hello","banana","car","machine","out")
man={
    0:("   ","   ","   "),
    1:(" o ","   ","   "),
    2:(" o "," | ","   "),
    3:(" o ","/| ","   "),
    4:(" o ","/|\\","   "),
    5:(" o ","/|\\","/  "),
    6:(" o ","/|\\","/ \\"),
}
def display_answer(answer):
    print(" ".join(answer))
def display_man(wrongguess):
    for line in man[wrongguess]:
        print(line)
def display_hint(hint):
    print(" ".join(hint))
def main():
    answer=random.choice(words)
    wrongguess=0
    hint=["_"]*len(answer)
    guessed_letters=set()
    is_running=True
    while is_running:
        display_man(wrongguess)
        display_hint(hint)
        guess=input("enter your guess")
        if len(guess)>1 or not guess.isalpha():
            print("invalid input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if guess==answer[i]:
                    hint[i]=guess
        else:
            wrongguess+=1

        if "_" not in hint:
            display_man(wrongguess)
            display_answer(answer)
            print("You Win!")
            is_running=False
        elif wrongguess>=len(man)-1:
            display_man(wrongguess)
            display_answer(answer)
            print("you Loose!")
            is_running=False
if __name__=="__main__":
    main()


