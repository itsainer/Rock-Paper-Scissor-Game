# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:16:13 2023

@author: user
"""

#%%

u1 = input("Hi, Player 1! Choose rock/scissors/paper: ")
u2 = input("Hi, Player 2! Choose rock/scissors/paper: ")

def game(p1,p2):
    
    if p1 == 'rock' and p2 == 'scissors':
        print("Player 1 wins :)")
        
    elif p1 == 'scissors' and p2 == 'rock':
        print("Player 2 wins :)")
        
    elif p1 == 'rock' and p2 == 'paper':
        print("Player 1 wins :)")
        
    elif p1 == 'paper' and p2 == 'rock':
        print("Player 2 wins :)")
        
    elif p1 == 'scissors' and p2 == 'paper':
        print("Player 1 wins :)")
        
    elif p1 == 'paper' and p2 == 'scissors':
        print("Player 2 wins :)")
        
    else:
        print("It is a draw!")
        
game(u1,u2)