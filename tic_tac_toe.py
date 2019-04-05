# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:29:27 2018

@author: mayur
"""
import random
from time import sleep
def input_player_letter(): # To get player letter
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
def draw_Board(board): # To draw the board
     print('   |   |')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |')
     
def first_player_pvc(): # To decide first player in player vs computer game
    
    if (random.randint(0,1) == 0):
        return 'Player'
    else:
        return 'Computer'
def first_player_pvp(): # To decide first player in player vs player game
    
    if (random.randint(0,1) == 0):
        return 'Player 1'
    else:
        return 'Player 2'
    
def replay():
    
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board,move, letter): # To make a move
    board[move] = letter
    
def is_win(b,l): # To check if one has won
    
    return ((b[7] == l and b[8] == l and b[9] == l) or
     (b[4] == l and b[5] == l and b[6] == l) or
     (b[1] == l and b[2] == l and b[3] == l) or
     (b[7] == l and b[4] == l and b[1] == l) or
     (b[8] == l and b[5] == l and b[2] == l) or
     (b[9] == l and b[6] == l and b[3] == l) or
     (b[7] == l and b[5] == l and b[3] == l) or
     (b[9] == l and b[5] == l and b[1] == l))
    
def is_space_free(board, move): # To check if space is free
    
    return board[move] == ' '

def player_move(board): # To get player move
    
    move = -1
    while (move not in list(range(1,10)) or not is_space_free(board, move)):
        try:
            move = int(input("Enter your next move (1-9)\n"))
        except:
            print("Please enter a number in the proper range")
    return move

def computer_move(board,computer_letter,player_letter): # subtle AI to decide computer move
    
    print("Computer's turn")
    for i in range(1,10):
        copy = board_copy(board)
        if is_space_free(copy,i):
            make_move(copy,i,computer_letter)
            if is_win(copy,computer_letter):
                return i
    for i in range(1,10):
        copy = board_copy(board)
        if is_space_free(copy,i):
            make_move(copy,i,player_letter)
            if is_win(copy,player_letter):
                return i
    move = random_move(board, [1,3,7,9])
    if move != None:
        return move
    if is_space_free(board, 5):
        return 5
    return random_move(board, [2,4,6,8])

def random_move(board, moves_list): # To perform a random move
    
    possible_moves=[]
    for i in moves_list:
        if is_space_free(board,i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None
    
def is_board_full(board): # To check if board is full
    
    for i in range(1,10):
        if is_space_free(board, i):
            return False
    return True
def board_copy(board):
    
    copy = []
    for i in board:
        copy.append(i)
    return copy

def t_t_t_pvc(): # The main pvc game
    
    c_score,p_score=0,0
    while (True):
        print("Scoreboard : Player Score : ",p_score,"Computer Score : ",c_score)
        m_board = [' ']*10
        player_letter, computer_letter = input_player_letter()
        turn = first_player_pvc()
        print(turn,"will go first")
        in_game=True
        while in_game:
            if turn == 'player':
                draw_Board(m_board)
                move = player_move(m_board)
                make_move(m_board, move, player_letter)
                if is_win(m_board, player_letter):
                    draw_Board(m_board)
                    print("Amazing! You have sucessfully defeated the computer.")
                    p_score+=1
                    in_game = False
                else:
                    if is_board_full(m_board):
                        draw_Board(m_board)
                        print("The game has ended in a tie")
                        in_game = False
                    else:
                        turn = 'computer'
            else:
                draw_Board(m_board)
                move = computer_move(m_board, computer_letter, player_letter)
                make_move(m_board, move, computer_letter)
                if is_win(m_board, computer_letter):
                    draw_Board(m_board)
                    print("You have lost. Don't worry, this was surely the computer's lucky day")
                    c_score+=1
                    in_game = False
                else:
                    if is_board_full(m_board):
                        draw_Board(m_board)
                        print("The game has ended in a tie")
                        in_game = False
                    else:
                        turn = 'player'
        if not replay():
            print("Final Score : Player Score : ",p_score,"Computer Score : ",c_score)
            break
        
def t_t_t_pvp(): # The main pvp game
    
    p1_score,p2_score=0,0
    while (True):
        print("Scoreboard : Player 1 Score : ",p1_score,"Player 2 Score : ",p2_score)
        m_board = [' ']*10
        player1_letter, player2_letter = input_player_letter()
        turn = first_player_pvp()
        print(turn,"will go first")
        in_game=True
        while in_game:
            if turn == 'Player 1':
                draw_Board(m_board)
                move = player_move(m_board)
                make_move(m_board, move, player1_letter)
                if is_win(m_board, player1_letter):
                    draw_Board(m_board)
                    print("Amazing! Player 1 wins.")
                    p1_score+=1
                    in_game = False
                else:
                    if is_board_full(m_board):
                        draw_Board(m_board)
                        print("The game has ended in a tie")
                        in_game = False
                    else:
                        turn = 'Player 2'
            else:
                draw_Board(m_board)
                move = player_move(m_board)
                make_move(m_board, move, player2_letter)
                if is_win(m_board, player2_letter):
                    draw_Board(m_board)
                    print("You have lost. Don't worry, this was surely the Player 2's lucky day")
                    p2_score+=1
                    in_game = False
                else:
                    if is_board_full(m_board):
                        draw_Board(m_board)
                        print("The game has ended in a tie")
                        in_game = False
                    else:
                        turn = 'Player 1'
        if not replay():
            print("Final Score : Player 1 Score : ",p1_score,"Player 2 Score : ",p2_score)
            break
def t_t_t():
    print("Let's play Tic Tac Toe")
    print("1: Player vs Player")
    print("2: Player vs Computer")
    print("3: Menu")
    print("Choose an option")
    d={1:t_t_t_pvp,2:t_t_t_pvc,3:lambda: None}
    try:
        d[int(input())]()
    except ValueError:
        print("Enter a valid number")
        sleep(2)
        print("\033[H\033[J")
        t_t_t()
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    