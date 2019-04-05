# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print(__name__)
from termcolor import cprint
import tic_tac_toe
import BlackJack
import Minion
from time import sleep 
import Handcricket
import rockpaperscissors
import pong
def menu():
    print("\033[H\033[J")
    try:    
        n=int(input("""Enter option number
                1:Rock Paper and Scissors
                2:Blackjack
                3:Tic Tac Toe
                4:Minion Game
                5:Handcricket
                6:Pong
                7:Exit\n"""))
        
    except Exception:
        print("Invalid input, please enter again")
        sleep(2)
        menu()
    try:
        choice(n)
        if(n!=7):
            menu()
    except UnboundLocalError:
        None
        
        
def choice(argument):
    switcher = {
        1: rockpaperscissors.game,
        2: BlackJack.main_menu,
        3: tic_tac_toe.t_t_t,
        4: Minion.info,
        5: Handcricket.game,
        6: pong.game,
        7: exit
    }
    
    func = switcher.get(argument, lambda: "Invalid Input")
    print("\033[H\033[J")
    func()
def m_m():
    
    print("\033[H\033[J")
    print("Hello there, Welcome to",end=" ");cprint("THE GAMING ARCADE",'red',end=" ");print("of the century!!!")
    print("With loads of free games to play, we promise you, you will never want to leave, ever!!!")
    input("Press Enter to continue")
    print("\033[H\033[J")
    menu()
    
m_m()