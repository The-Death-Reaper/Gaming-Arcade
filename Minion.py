# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 20:03:23 2018

@author: mayur
"""
print(__name__)
from time import sleep
def minion_game_1(string):
    points_p1,points_p2=0,0
    for i in range(len(string)):
        if (string[i]=='A' or string[i]=='E'or string[i]=='I'or string[i]=='O'or string[i]=='U'):
            points_p1+=len(string)-i
        else:
            points_p2+=len(string)-i
    if(points_p1>points_p2):
        print("Player 1 wins with points",points_p1)
    elif(points_p1<points_p2):
        print("Player 2 wins with points",points_p2)
    else:
        print("Draw")
    play_again()
def minion_game_2(string):
    points_p1,points_p2=0,0
    for i in range(len(string)):
        if (string[i]=='A' or string[i]=='E'or string[i]=='I'or string[i]=='O'or string[i]=='U'):
            points_p2+=len(string)-i
        else:
            points_p1+=len(string)-i
    if(points_p1>points_p2):
        print("Player 1 wins with points",points_p1)
    elif(points_p1<points_p2):
        print("Player 2 wins with points",points_p2)
    else:
        print("Draw")
    play_again()

def info():
    print("In this game, the two players randomly enter a word or string. The objective of this game is to get maximum number of substrings beginning with consonants and vowels. Player 1 can choose which he wants to do so before hand.")
    print("A player gets +1 point for each occurrence of the substring in the string.")
    try:
        c1=int(input("Start game ? Click 1 \nMain Menu ? Click 2\n"))
    except ValueError:
        print("Enter a valid number")
        sleep(2)
        print("\033[H\033[J")
        info()
        return
    choice1={1: begin , 2: lambda: None}    
    func1=choice1.get(c1, lambda: invalid())
    func1()
def invalid():
    print("Invalid Input")
    info()
def begin():
    s=input("Player 1, please enter the type of substring you would like to make, starting with vowel or consonant.\n")
    s1=input("Enter the String \n").upper()
    if s.startswith("v"):
        minion_game_1(s1)
    elif s.startswith("c"):
        minion_game_2(s1)
    
def play_again():
    s=input("Do you want to play again?")
    if s.startswith('y'):
        begin()
    else:
        return None
    