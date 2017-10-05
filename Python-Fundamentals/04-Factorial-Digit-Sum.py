#Problem Set 4
#Adrian Golias

#Importing libraries
import math

#Output of factorial of 100
print(math.factorial(100))

#Declaration of variable to store a factorial value
n = math.factorial(100)

#Declaration of the list of numbers, which is populated from
#a string containing long number from 100!
numbers = [int(d) for d in str(n)]

#Output of the whole list array
print(numbers)

# Print the sum of the digits in the number 100!
print(sum(numbers))