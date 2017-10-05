#Problem Set 3
#Adrian Golias

#Declaration of the for loop
for num in range(1,101):
    #If the # is a multiple of three
	if num % 3 == 0:
		#Output Fizz message to the screen
		print("Fizz")
		
    #Else if the # is a multiple of five
	elif num % 5 == 0:
		#Output Buzz message to the screen
		print("Buzz")
		
	#Else if the # is a multiple of both both three and five
	elif num % 5 == 0 and num % 3 == 0:
		#Output FizzBuzz message to the screen
		print("FizzBuzz")
		
    #Else when the # is neither of above
	else:
		#Output that number in a message to the screen
		print(num)