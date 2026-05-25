import random

guesses=0
highest_num=100
lowest_num=1
ongoing=True
num=random.randint(lowest_num,highest_num)
while ongoing:
    guess=input(f"enter your guess between {highest_num} and {lowest_num}: ")
    guesses+=1
    if guess.isdigit():
        guess=int(guess)
        if guess<highest_num and guess>lowest_num:
            if guess>num:
                print("Too high. TRY AGAIN.")
            elif guess<num:
                print("Too low. TRY AGAIN")
            else:
                print("YAY! YOU GOT IT")
                break
        else:
            print("please enter a valid input in range {lowest_num} and {highest_num}")
    else:
        print(f"That is invalid input. please enter a valid input in range {lowest_num} and {highest_num}")
print(f"your took {guesses} guesses to find it")