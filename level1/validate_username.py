#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username=input("enter user name: ")
if len(username)>12:
    print("the username length must not be greater than 12 charecters")
elif username.count(" ")>0:
    print("the username should not contain spaces")
elif username.isalpha()==False:
    print("username must not contain any digits")
else:
    print(f"welome {username}")