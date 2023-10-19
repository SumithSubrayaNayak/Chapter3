import random
secretNumber = random.randint(1,20)
print('I am considering number between 1 to 20')

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess= int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess>secretNumber:
        print('Your guess is too high')
    else:
        break #This condition is the correct guess

if guess == secretNumber:
    print('Good job! You guessed my number in '+ str(guessesTaken) +' guesses!')
else:
    print('Nope. The number I was thinking of was'+ str(secretNumber))
    