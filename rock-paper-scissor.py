import random
rps=["ROCK","PAPER","SCISSORS"]
minval=0
maxval=2
player=input("rock/paper/scissors?:").upper()
computer=random.randint(minval,maxval)
print(rps[computer])
if rps[computer]==player:
    print("TIE")
else:
    if rps[computer]=="ROCK":
        if player=="SCISSORS":
            print("YOU LOSE")
        elif player=="PAPER":
            print("YOU WIN")
    elif rps[computer]=="PAPER":
        if player=="SCISSORS":
            print("YOU WIN")
        elif player=="ROCK":
            print("YOU LOSE")
    elif rps[computer]=="SCISSOR":
        if player=="PAPER":
            print("YOU LOSE")
        elif player=="ROCK":
            print("YOU WIN")
