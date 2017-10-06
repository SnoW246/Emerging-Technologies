#Problem Set 8
#Adrian Golias

#Initialization of two sorted list arrays with initial element values
list1 = [2, 8, 12]
list2 = [4, 6, 10]

#Output two lists to the screen
print("This is sorted list #1", list1)
print("This is sorted list #2", list2)

#Declaration of a veriable to merge the lists together
mergedList = list1 + list2

#Output merged list to the screen
print("Merged list: ", mergedList)
#Output sorted merged list to the screen
print("Merged & sorted list: ", sorted(mergedList))
#Output reversed sorted list to the screen
print("Merged & reverse sorted", sorted(mergedList, reverse=True))