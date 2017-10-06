#Problem Set 9
#Adrian Golias

#Impoting libraries
import math

#Declaration of a veriable and initializing it with a value
x = 6.0

#Declaration of Newton's method of square root
z_next = lambda z: (z - ((z*z - x) / (2 * z)))

#Declaration of a current
current = 1.0

#While loop to keep increasing the current 
while current != z_next(current):
	#
	current = z_next(current)
#Output of messages to the screen with 
#Math & Newthon's square root method
print("Square root of X using Math Library:    ", math.sqrt(x))
print("Square root of X using Newton's method: ", current)
