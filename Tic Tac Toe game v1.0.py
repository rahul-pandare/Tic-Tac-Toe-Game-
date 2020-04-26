#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to the Game of TIC-TAC-TOE!")

#importing required libraries
from IPython.display import clear_output #To clear the output
from colorama import Fore, Back, Style #For text colour
import random #In order to choose a random player to go first

#Function for printing the game table or chart
def frame(a):
    clear_output()
    print('      |      |      ')
    print('  '+ a[7] +'   |   '+ a[8] +'  |   '+ a[9]+'   ')
    print('______|______|______')

    print('      |      |      ')
    print('  '+ a[4]+'   |   '+ a[5]+'  |   '+ a[6]+'   ')
    print('______|______|______')

    print('      |      |      ')
    print('  '+ a[1]+'   |   '+ a[2]+'  |   '+ a[3]+'   ')
    print('      |      |      ')

#Function for printing the game table or chart
def frame1(a):
    print('      |      |      ')
    print('  '+ a[7] +'   |   '+ a[8] +'  |   '+ a[9]+'   ')
    print('______|______|______')

    print('      |      |      ')
    print('  '+ a[4]+'   |   '+ a[5]+'  |   '+ a[6]+'   ')
    print('______|______|______')

    print('      |      |      ')
    print('  '+ a[1]+'   |   '+ a[2]+'  |   '+ a[3]+'   ')
    print('      |      |      ')

# To check win conditions
def wincon():
    return (c[1] == c[2] == c[3] or
               c[4] == c[5] == c[6] or
               c[7] == c[8] == c[9] or
           
               c[1] == c[4] == c[7] or
               c[2] == c[5] == c[8] or
               c[3] == c[6] == c[9] or
           
               c[1] == c[5] == c[9] or
               c[3] == c[5] == c[7])

# To check win conditions against a marker
def winconp(mark):
    return (c[1] == c[2] == c[3] == mark or
                c[4] == c[5] == c[6] == mark or
                c[7] == c[8] == c[9] == mark or
           
                c[1] == c[4] == c[7] == mark or
                c[2] == c[5] == c[8] == mark or
                c[3] == c[6] == c[9] == mark or
           
                c[1] == c[5] == c[9] == mark or
                c[3] == c[5] == c[7] == mark)

#display score board
def score():
    lenp1win = (len(p1win)*2) + len(tie)
    lenp2win = (len(p2win)*2) + len(tie)
    
    if lenp1win < 10:
        print('\n')
        print('     '+ player1 +'        '+ player2 )
        print('____________|____________')

        print('            |            ')
        print('     '+ str(lenp1win) +'      |     '+ str(lenp2win) + '       ')
        print('            |            ')
    else:
        print('\n')
        print('     '+ player1 +'         '+ player2 )
        print('____________|____________')

        print('            |            ')
        print('     '+ str(lenp1win) +'     |     '+ str(lenp2win) + '       ')
        print('            |            ')

# Lists for score
p1win = []  
p2win = []
tie=[]

#Input player names
player1=(input('\nPlayer 1 input your name: ').capitalize())
player2=(input('\nPlayer 2 input your name: ').capitalize())

p1=(input(f'\n{player1} do you want to be X or O ?:' ).upper())

while p1[0] not in ('X','O'):
    print('\nCharacter not recognised')
    p1=(input(f'\n{player1} do you want to be X or O:' ).upper())

    
if p1[0] == 'X':
    p2 ='O'
    p1 = 'X'
else:
    p2 ='X'
    p1 = 'O'

clear_output()

again=True

#Game loop
while again:
    clear_output()
    a = [' '," "," "," "," "," "," "," "," "," "]
    c = [' ',"1","2","3","4","5","6","7","8","9"]
    print("\nLet's begin the game!")
    print("\nWinner gets 2 points. If it\'s a tie both players get 1 point.'")
    print("\nThis is the matrix and the position numbers:")
    frame1(c)

    #To decide which player will go randomly
    flip=random.randint(0,1)

    if flip==0:
        k=player1
        j=player2
        print(f'\n{k} will go first')
    
    elif flip==1:
        k=player2
        j=player1
        print(f'\n{k} will go first')

    b=[] #To check if a game is tied

    while not wincon():
    
        #While loop to get valid input from player
        p1i='dv'
        while p1i not in range(1,10):
            try:
                p1i=int(input(f'\n{k} choose your next position (1-9): '))
            except ValueError:
                print("\nPosition chosen is invalid. Choose a position between 1-9")
                continue
        
        #Promt if a position is already taken
        while a[p1i] != " ":
            print("\nPosition is already taken")
            p1i='dv'
            while p1i not in range(1,10):
                try:
                    p1i=int(input(f'\n{k} choose your next position (1-9): '))
                except ValueError:
                    print("\nPosition chosen is invalid. Choose a position between 1-9")
                    continue
        #Depending who was the first player the position gets appended to list b
        if k==player1:
            c[p1i] = p1
            a[p1i] = p1
            b.append(p1i)
        else:
            c[p1i] = p2
            a[p1i] = p2
            b.append(p1i)
              
        frame(a)
    
        if k==player1:
            if winconp(p1):
                print(f'\nCongratulations! {k} has won.')
                p1win.append(1)
                break
            elif len(b) == 9:
                print('\nIt\'s a tie!')
                tie.append(1)
                break

        else:
            if winconp(p2):
                print(f'\nCongratulations! {k} has won.')
                p2win.append(1)
                break
            elif len(b) == 9:
                print('\nIt\'s a tie!')
                tie.append(1)
                break
                
        #While loop to get valid input from player
        p2i='dv'
        while p2i not in range(1,10):
            try:
                p2i= int(input(f'\n{j} choose your next position (1-9): '))
            except ValueError:
                print("\nPosition chosen is invalid. Choose a position between 1-9")
                continue
    
        #Promt if a position is already taken
        while a[p2i] != " ":
            print("\nPosition is already taken")
            p2i='dv'
            while p2i not in range(1,10):
                try:
                    p2i= int(input(f'\n{j} choose your next position (1-9): '))
                except ValueError:
                    print("\nPosition chosen is invalid. Choose a position between 1-9")
                    continue
        
        #Depending who was the first player the position gets appended to list b
        if j==player1:
            c[p2i] = p1
            a[p2i] = p1
            b.append(p1i)
        else:
            c[p2i] = p2
            a[p2i] = p2
            b.append(p2i)
        frame(a)
        
        # To check the game outcome
        if k==player1:
            if winconp(p2):
                print(f'\nCongratulations! {j} has won.')
                p2win.append(1)
                break
            elif len(b) == 9:
                print('\nIt\'s a tie!')
                tie.append(1)
                break

        else:
            if winconp(p1):
                print(f'\nCongratulations! {j} has won.')
                p1win.append(1)
                break
            elif len(b) == 9:
                print('\nIt\'s a tie!')
                tie.append(1)
                break
    #Print score board        
    print("\nScore Board:")
    score()
    choice=input('\nDo you wish to play again? Y or N:').upper()  #Prompt for playing again
    if choice == 'Y':
        again=True  # since it is true the while loop runs again
        continue
    else:
        again=False
        print('\nOkay, Thank you for playing!')

#Hit Shift + Enter to begin


# In[ ]:




