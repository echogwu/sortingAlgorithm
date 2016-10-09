#!/usr/bin/python

# Binary Search is used for ORDERED list
#
##############################################
# Found <- False
# while not Found and first <= top
#     Midpoint <- (First + Last) DIV 2
#     If List[Midpoint] = ItemSought Then
#         ItemFound <- True
#     Else
#         If First >= Last Then
#             SearchFailed <- True
#         Else
#             If List[Midpoint] > ItemSought Then
#                 Last <- Midpoint - 1
#             Else
#                 First <- Midpoint + 1
#             EndIf
#         EndIf
#     EndIf
##############################################
#

def binarySearch(myItem, myList):
    midPoint = 0
    first = 0
    last = len(myList) - 1
    found = False
    counter = 0
    while last >= first and not found:
        counter += 1
        midPoint = (last + first) / 2
        print("first = %d, midPoint = %d, last = %d" % (first, midPoint, last))
        if myItem == myList[midPoint]:
	    found = True
            print("the position is %d" % midPoint)
	if myItem > myList[midPoint]:
	    first = midPoint + 1
	if myItem < myList[midPoint]:
	    last = midPoint - 1
    print("It takes %d searches" % counter)
    return found

myList = [0,1,2,3,4,5,6,7,8,9,10]
myItem = 9
isFound = binarySearch(myItem, myList)
if not isFound:
    print("the item %s is not in the list" % myItem) 
