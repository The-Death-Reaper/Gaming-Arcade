from time import sleep
ucount=0
ccount=0
def game(): 
    try:
        c1=int(input("Start game ? Click 1 \nMain Menu ? Click 2\n"))
    except ValueError:
        print("Enter a valid number")
        sleep(2)
        print("\033[H\033[J")
        game()
        return
    choice1={1: play , 2: lambda: None}    
    func1=choice1.get(c1, lambda: invalid())
    func1()
def invalid():
    print("Invalid Input")
    game()
def play():
    global ucount
    global ccount
    import random
    symbols=["rock", "paper", "scissor"]
    
    usym=input("Enter Your Symbol\n").lower()
    if usym in symbols:
        csym=random.choice(symbols).lower()
        print("Computer chooses ", csym)
        if usym=="rock":
            if csym.startswith("r"):
                print("TIE !")
            elif csym.startswith("p"):
                    print("YOU LOSE !")
                    ccount=ccount+1
            else:
                print("YOU WIN !")
                ucount=ucount+1
        elif usym=="paper":
            if csym.startswith("p"):
                print("TIE !")
            elif csym.startswith("s"):
                print("YOU LOSE !")
                ccount=ccount+1
            else:
                print("YOU WIN !")
                ucount=ucount+1
        elif usym=="scissor":
            if csym.startswith("s"):
                print("TIE !")
            elif csym.startswith("r"):
                print("YOU LOSE !")
                ccount=ccount+1
            else:
                print("YOU WIN !")
                ucount=ucount+1
        print("Your score : ", ucount, "Computer's score : ", ccount)
        choice2={1: play, 2: game}
        try:
            c2=int(input("Play again ? Click 1\nMenu ? Click 2\n"))
        except ValueError:
            print("invalid option")
            game()
        func2=choice2.get(c2, "Invalid Input !")
        func2()
    else:
        print("Invalid symbol ! Or check your spelling.")
        choice2={1: play, 2: game}
        try:
            c2=int(input("Play again ? Click 1\nMenu ? Click 2\n"))
        except ValueError:
            print("invalid option")
            game()
        func2=choice2.get(c2, lambda: print("Invalid Input !"))
        func2()
    
    
            
            
    
 
    
