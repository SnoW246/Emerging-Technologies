#Problem Set 6
#Adrian Golias

#Initialization of empty array list
list = []

#Outputing message to prompt user for input
print("Please input 15 random numbers into the list")
#Declaration of for loop to iterate through 15 inputs
for n in range(15):
	#Declaration of a variable to take in user input each time
    numbers = int(input('Enter new number: '))
	#Add user input to the list
    list.append(numbers)
#Outputing message to the screen to display smallest
# & highest element from the list
print("Smallest: ", min(list), "\nLargest: ", max(list))