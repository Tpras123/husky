import random
print("*******ROCK PAPER SCISSORS*******")


comp_choice=["paper","rock","scissors","PAPER","ROCK","SCISSORS","p","s","r","R","S","P"]

p=0
c=0




while p<3 and c<3:
    us_choice = input("enter scissors or rock or paper: ")
    comp_choice = random.choice(["paper", "rock", "scissors", "PAPER", "ROCK", "SCISSORS"])

    if us_choice == comp_choice:
        print("it's tie! no points")

    elif (us_choice == "ROCK" or us_choice == "R" or us_choice == "r" or us_choice == "rock" ):
        if (comp_choice == "scissors" or comp_choice == "SCISSORS" or comp_choice == "S" or comp_choice == "s"):
           print("user won! one point!")
           p = p + 1
        elif (comp_choice == "paper" or comp_choice == "p" or comp_choice == "P" or comp_choice == "PAPER"):
            print("computer won! one point!")
            c = c + 1
    elif (us_choice == "PAPER" or us_choice == "paper" or us_choice == "p" or us_choice == "P"):
        if (comp_choice == "scissors" or comp_choice == "SCISSORS" or comp_choice == "S" or comp_choice == "s"):
           print("computer won! one point!")
           c = c + 1
        elif (comp_choice == "rock" or comp_choice == "r" or comp_choice == "R" or comp_choice == "ROCK"):
            print("user won! one point!")
            p = p + 1
    elif (us_choice == "SCISSORS" or us_choice == "scissors" or us_choice == "s" or us_choice == "S"):
            if (comp_choice == "paper" or comp_choice == "PAPER" or comp_choice == "p" or comp_choice == "P"):
                print("user won! one point!")
                p = p + 1
            elif (comp_choice == "rock" or comp_choice == "r" or comp_choice == "ROCK" or comp_choice == "R"):
                print("computer won! one point!")
                c = c + 1
    else:
        print("INVALID CHOICE")

if p > c:
    print("you won by "+str(p))
else:
    print("computer won by "+str(c))

