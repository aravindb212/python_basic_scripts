## guess the number game
import random
print ("Hello..! Welcome to guess the number game whats your name: ")
name=input()
print('Well, '+ name + ' im thinking of a number between 1 to 30')

secretNumber= random.randint(0,30)
for guessTaken in range (1,8):
    print('Take a guess..')
    guess= int(input())

    if guess > secretNumber:
        print('your guess is too high')
    elif guess < secretNumber:
        print('your guess is too low')
    else:
        break #correct guess

if guess== secretNumber:
    print('Great..! '+ name + '! you guessed my number  '+ str(guessTaken) + ' guesses')
else:
    print('Sorry.. guesses exceeded... the number i was thinking '+ str(secretNumber))    
print('you took '+ str(guessTaken)+ ' guesses.')
