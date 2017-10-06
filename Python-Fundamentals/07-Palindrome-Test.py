#Problem Set 7
#Adrian Golias

#Output instruction message to the screen and prompt user for input
print("Please input a word to check for palindrome: ")
#Take user input
word = input()
#Make user input lowercase
word = word.casefold()
#If arguement to chack if the word is equal 
#to reversed version of itself
if(word == word[::-1]):
	#Output message to the screen when word matches its inverted self
	print("'" + word + "' word is a palindrome!")
#Else if word doesn't match its inverted self, output message to the screen if word
else:
	print("Unfortunately '" + word + "' isn't a palindrome..")