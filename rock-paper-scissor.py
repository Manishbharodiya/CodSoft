import random 
options = ("rock","paper","scissors")

running = True
count=0
lose=0

while running:

    
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock , paper, scissors) : ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")


    if player == computer:
        print("It's a Tie! ")

    elif player == "rock" and computer=="scissors" :
        print("You Win !")
        count=count+1

    elif player=="paper" and computer=="rock":
        print("You Win !")
        count=count+1

    elif player=="scissors" and computer=="paper" :
        print("You Win !")
        count=count+1

    else:
        print("You Lose !")
        lose= lose+1

    play_again =  input("play Again? (y/n) : ").lower() 
    if not play_again =="y" :
        running = False


if count > lose:
    print(f"player win {count} matches")
elif count==lose:
    print("both wins {count} matches! so its a tie....")
else:
    print(f"Computer win {lose} matches")
print("Thanks for Playing")