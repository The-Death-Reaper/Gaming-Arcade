import random

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

def deal(deck):         #To deal the inital cards to player and dealer

    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "Jack"
        if card == 12:
            card = "Queen"
        if card == 13:
            card = "King"
        if card == 14:
            card = "Ace"
        hand.append(card)
    return(hand)

def hit(hand):          #To give the player/dealer an extra card

    card = deck.pop()
    if card == 11:
        card = "Jack"
    if card == 12:
        card = "Queen"
    if card == 13:
        card = "King"
    if card == 14:
        card = "Ace"
    hand.append(card)
    return(hand)

def total(hand):            #To calculate the total sum of the player/dealers hand

    total = 0
    for i in hand:
        if i == 'Jack' or i == 'Queen' or i == 'King':
            total+=10
        elif i == 'Ace':
            if total >= 11:
                total+=1
            else:
                total+=11
        else:
            total += i

    return(total)

def check(player,dealer):           #To check who has a larger sum total of their cards
    
    if dealer > player and dealer < 21:
        print("Sorry you Lost ")
        winnings(0)
    elif dealer < player and player < 21:
        print("You won !!")
        winnings(1)
    elif dealer == player:
        print("It's a draw, no one wins or loses ")
        winnings(2)

def bets():            #Place bets
    global bet
    global money
    bet=0
    print("How much do you bet this round ?")
    bet=int(input())
    if bet > money:
        print("Insufficient funds, try again ")
        bets()
    else:
        money = money-bet
    print("The total bet for this round is ",bet*2)
    print("You have ",money,"monies left ")
    print("Good luck ")


def winnings(n):            #to calculate whether player has won or lost money
    global bet
    global money
    if n == 1:
        print("Since you won the round, you win ",bet*2,"amount of money !!!")
        money = money + bet*2
        print("Your total amount is now ",money,"monies")
    elif n==2:
        print("You drew with the dealer ! You do not lose any money this round ")
        money = money+bet
    else:
        print("You lost that round, hence losing ",bet,"amount of money ")
        print("You now have ",money,"monies left ")
    
def main():         #main body of the program, game takes place here

    player = deal(deck)
    dealer = deal(deck)
    op = 'k'
    bets()
    while op != 'yes' or op != 'Yes' or op != 'y' or op != 'Y':
        print("Your cards are :",player,"\nThe dealer has been dealt", dealer[0], "and another unknown card(s)")
        print("Your total is currently ",total(player),".Would you like to hit for another card ?(yes/no)")
        op=input() 
        if op == 'yes' or op == 'Yes' or op == 'y' or op == 'Y':
            hit(player)
            if total(player) == 21:
                print("You have cards: ",player)
                print("You got a blackJack, you win !!")
                winnings(1)
                break
            elif total(player) > 21:
                print("You have cards: ",player)
                print("You went bust, you lose ")
                winnings(0)
                break
        else:
            print("The dealer is now playing...")
            while total(dealer) <= 17:
                hit(dealer)
            print("The dealer has the value ",total(dealer))

            if total(dealer) == 21:
                print("Dealer has cards: ",dealer)
                print("Dealer got a blackJack !! You lose ")
                winnings(0)
                break
            elif total(dealer) > 21:
                print("Dealer has cards: ",dealer)
                print("Dealer went bust, you win ! ")
                winnings(1)
                break
            check(total(player),total(dealer))
            break
        
def cls():              #clear the screen
    print("\033[H\033[J")
    
def rules():            #Print the rules on how to play
    print("Rules:\n")
    print("The objective of BlackJack is to get (or get as close to) a sum of 21 using your cards.")
    print("You and the dealer are delt two cards each, you can see both your cards but you can only see one card of the dealers")
    print("You can 'hit' to get another card but beware, going over the sum of 21 results in a 'bust' where you automatically lose")
    print("The game is between you and the dealer, but the dealer can win too !")
    print("\nYou have 1,000 monies with you to start off, you can keep playing as long as you have atleast 50 monies")
    print("Good luck ")
    
global money
money=1000

def filewrite():                #write the total score of the player
    obj = open("Monies.txt",'a')
    global money
    name=input("Enter your username \n")
    obj.write("\n")
    obj.write(name)
    obj.write(" ")
    obj.write(str(money))
    print("Your details have been saved ")
    obj.close()

def checkmoney():
    print("You have ",money," monies left ")



    
def fileread():                 #Display all the scores
    obj = open("Monies.txt",'r')
    global money
    print("Leaderboards :")
    print(obj.read())
    obj.close()

def menu():
    n=0;op=0
    print("Menu:")
    print("1.Play Game")
    print("2.Check Rules")
    print("3.Enter Leaderboards")
    print("4.Check Leaderboards")
    print("5.Check Money")
    print("6.Exit Game")
    print("Please enter an option :  ")
    n = int(input())

    if n==1:
        if money <= 50:
            print("Insufficient funds")
        else:
            main()
            op=input()
            cls()

    elif n==2:
        rules()
        op=input()
        cls()
        menu()

    elif n==3:
        filewrite()
        op=input()
        cls()
        menu()

    elif n==4:
        fileread()
        op=input()
        cls()
        menu()

    elif n==5:
        checkmoney()
        op=input()
        cls()
        menu()

    elif n==6:
        print("Goodbye")
        return

    else:
        print("Invalid Entry try again \n")
        menu()


def main_menu():
    print("Welcome to BlackJack !!")
    opop = 'yes'
    while opop == 'yes' or opop == 'Yes' or opop == 'y' or opop == 'Y':
        menu()
        print("Would you like to return to main menu ?")
        opop=input()
        if opop == 'yes' or opop == 'Yes' or opop == 'y' or opop == 'Y' :
            deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
            print("Exiting game ")
            return
        else:
            menu()

    












        

    
