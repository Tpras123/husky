from tkinter  import *
import random

t=Tk()
t.geometry('500x600')
t.config(bg = "black")
t.title('************ Rock,paper & scissors game: *************')
user = StringVar()
Label(t,text = "Enter rock or paper or paper:",font='arial 12 bold',fg = "brown", bg = 'orange'  ,width = "70").pack()

Entry(t,font = 'arial 15 bold',textvariable = user,bg = "green").place(x=140,y=40)

comp_choice = random.choice(["paper", "rock", "scissors", "PAPER", "ROCK", "SCISSORS","p","r","s","P","R","S"])


Res = StringVar()


def click():

    us_choice = user.get()

    if us_choice == comp_choice:
            Res.set("it's tie! no points")

    elif (us_choice == "ROCK" or us_choice == "R" or us_choice == "r" or us_choice == "rock" ):
             if (comp_choice == "scissors" or comp_choice == "SCISSORS" or comp_choice == "S" or comp_choice == "s"):
                  Res.set("user won! one point!")

             elif (comp_choice == "paper" or comp_choice == "p" or comp_choice == "P" or comp_choice == "PAPER"):
                Res.set("computer won! one point!")

    elif (us_choice == "PAPER" or us_choice == "paper" or us_choice == "p" or us_choice == "P"):
             if (comp_choice == "scissors" or comp_choice == "SCISSORS" or comp_choice == "S" or comp_choice == "s"):
                   Res.set("computer won! one point!")

             elif (comp_choice == "rock" or comp_choice == "r" or comp_choice == "R" or comp_choice == "ROCK"):
                    Res.set("user won! one point!")

    elif (us_choice == "SCISSORS" or us_choice == "scissors" or us_choice == "s" or us_choice == "S"):
            if (comp_choice == "paper" or comp_choice == "PAPER" or comp_choice == "p" or comp_choice == "P"):
                Res.set("user won! one point!")

            elif (comp_choice == "rock" or comp_choice == "r" or comp_choice == "ROCK" or comp_choice == "R"):
                Res.set("computer won! one point!")


    else:
         Res.set("INVALID CHOICE")

def Reset():
    Res.set("")
    user.set("")
Entry(t,font = 'arial 12 bold' , textvariable = Res,bg = "yellow" ,width = "40",).place(x = 50, y =100)
Button(t,font = 'arial 10 bold',bg = "blue" ,text = "play" ,command = click).place(x = 150, y =70)
Button(t,font = 'arial 10 bold',bg = "red" ,text = "play again" ,command = Reset).place(x = 300, y =70)

t.mainloop()
