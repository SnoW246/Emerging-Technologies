#Problem Set 2
#Adrian Golias

#Importing libraries
import time;

#Declaration of local variable that returns time-tuple
currentTimeDate = time.localtime(time.time())
#Output of current time-tuple to the screen /unformatted
print("Current local time is: ", currentTimeDate)

#Declaration of local variable that returns formatted time-tuple
currentTimeDate = time.asctime(time.localtime(time.time()))
#Output of formatted current time-tuple which is easy to read
print("Current local time is: ", currentTimeDate)