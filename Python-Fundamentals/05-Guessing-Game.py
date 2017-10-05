#Problem Set 5
#Adrian Golias

#Import libraries
import random

#Declaration of count variable and assigning it a value of 1
countGuesses = 1
#Declaration of a variable and assigning it a random value between 1 & 20
randomNumber = random.randint(1, 20)

#Output message with instructions to the screen
print('Guess a number between 1 and 20')
#Take user input
guess = input()
#Convert user input from string value to an integer value
guess = int(guess)

#If user guess is lower than random number
if guess < randomNumber:
	#Output message to the screen
	print('Your guess is too low')

#If user guess is higher than random number
if guess > randomNumber:
	#Output message to the screen
	print('Your guess is too high')

#While loop to allow guessing until guess matched
while guess != randomNumber:
	#Output message to try again
	print('Try again!')
	#Take user input
	guess = input()
	#Convert user input from string value to an integer value
	guess = int(guess)
	
	#Increase number of guesses taken
	countGuesses += 1
	
	#If user guess is lower than random number
	if guess < randomNumber:
		print('Your guess is too low')
	
	#If user guess is higher than random number
	if guess > randomNumber:
		print('Your guess is too high')
	
	#If user guess is matched with random number generated
	if guess == randomNumber:
		#Break out of the loop
		break

#If user guess is matched with random number generated
if guess == randomNumber:
	#Convert number of guesses taken into string
	countGuesses = str(countGuesses)
	#Output message to the screen informing user how many tries were taken
	print('Great! You have guessed the number in ' + countGuesses + ' guesses!')