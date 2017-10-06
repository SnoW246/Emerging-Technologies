#Problem Set 10
#Adrian Golias

#Declaration of a function to reverse a string
def reverse(string): 
	#Declaration of a temporary string to hold reversed string
    tempString = reversed(string)
	#Function return reversed string using join, 
	#to force evaluate the iterator
    return ''.join(tempString)

#Output of message to the screen
print("Please input a string you wish to reverse: ")
#Take user input
userString = input()
#Output of message to the screen with reversed string
print (reverse(userString))