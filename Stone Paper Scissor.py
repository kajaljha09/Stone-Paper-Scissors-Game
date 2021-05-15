print("_______WELCOME TO STONE PAPER SCISSORS GAME_______")
print("Here you will be competing with the Computer")
print("So lets get ready to fight :)")
print("************************************************************")
print("                                                             ")
print("Game rules:")
print("A:You have to choose among the following:")
print("                                  1.Stone   2.Paper    3.Scissors")
print("B:You will get ten chances and you will get 1 pt for winning and 0 pt for loosing.\tAt the end total will be calculated who has highest will be declared winner ")
i=1
k=0
b=0
while (i<=10):
    game=["Stone","Paper","Scissors"]
    c=input("Your chance:")
    chance=c.capitalize()

    import random
    a=random.choice(game)
    print("Computer chance:",a)
    if (a=="Stone" and chance=="Paper") or (a=="Paper" and chance=="Scissors") or (a=="Scissors" and chance=="Stone"):
        k=k+1
        print("You won ,ur pt is",k)
    elif (a=="Stone" and chance=="Scissors") or (a=="Scissors" and chance=="Paper") or (a=="Paper" and chance=="Stone"):
        b=b+1
        print("You loose")
    elif  (a=="Stone" and chance=="Stone") or (a=="Scissors" and chance=="Scissors") or (a=="Paper" and chance=="Paper"):
        print("This is tie")
    else:
        print("Invalid Syntax Entered")

    i=i+1
if k>b:
    print("Congratulations You Won")
    print("Your score",k)
    print("You won by",k-b)
elif k<b:
    print("You loose, Don't Worry Try Next Time" )
    print("your score",k)
elif k==b:
    print("Game tie")
else:
    print("Good Day")

