# File- uopsp_assignment1_sinty019. py
# Author: Taranjot Singh
# Email id: Sinty019@mymail.unisa.edu.au
# Description: Programming Assignment 1:Petals Around the Rose
# This is my own work as described by the university's ]
# Academic Misconduct policy
# Date: 18/10/2020

# Putting the detailes of company
name ='Petals Around the Rose'

# under lining the name
under_line = '-'*len(name)

#putting the message on
message = ('The name of the game is \'Petals Around the Rose\'. The name of the game is important.'
         'The computer will roll five dice and ask you to guess the score for the roll. The score'
         'will always be zero or an even number. Your mission, should you choose to accept it, is to work out'
         'how the computer calculate the score. If you succed in working out the secret and guess the score.'
         'if you succeed in working out the secret and guess correctly four times in row, you become a Potentate of Rose')
print(name)
print(under_line)
print(message)

# importing the random number
import random

import dice


# count to see the number of game
count = 0 

# To represent the start after the die representation.
star =' # '

# To see how many correct answers has been given continually.
correction = 0

# To see how many correct answers has been given  in whole loop 
correct_ans=0



# Asking the user for game
user = input('Would you like to play Petals Around the Rose [y/n]?  ')

# while loop just in case user put other then y or n
while user != 'y' and user != 'Y' and user != 'n' and user != 'N':
    user = input('Please enter either\'y\' or \'n\':  ')


 # Putting the while loop
 
while user=='y':
    count+=1

    # Asking for random number for diced
    die1 = random.randint(1,6)

    die2 = random.randint(1,6)

    
    die3 = random.randint(1,6)

        
    die4 = random.randint(1,6)
  
    die5 = random.randint(1,6)


    dice.display_dice(die1, die2, die3, die4, die5)

    

    

    # Making the numbers even for the even result
    
    if die1 % 2 == 1:
        die1 = die1 - 1
        
        
    if die2 % 2 == 1:
        die2 = die2 - 1
        
        
    if die3 % 2 == 1:
        die3 = die3 - 1
        
        
    if die4 % 2 == 1:
        die4 = die4 - 1
        
        
    if die5 % 2 == 1:
        die5 = die5 - 1

    die6 = die1 + die2 + die3 + die4 + die5


    # asking user to guess the number
    guess = int(input('Please Guess: '))


    
    # Putting the if loop to display the answers
    if guess == die6:
        correction += 1
        correct_ans+=1
        print('Well done! You guessed it')
        if correction == 4:
            print('You have found the secret')
            print('Do not tell any body')
    elif guess % 2 != 0:
        print('number will be even always')

    elif guess != die6:
        correction=correction-correction
        print('No sorry, it\'s[',die6,']not[',guess,']')

    user=input('Roll dice again[y/n]? ')
print('You have played:',count,'times.')
print('You have guessed:',correct_ans,'correct times.')

    
    
    

