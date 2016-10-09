#!/usr/bin/python

#
########################################################
# from http://www.pythonschool.net/data-structures-algorithms/bubble-sort/
# Repeat
#    X <- StartofArray
#    Flag <- False
#    Repeat
#        If Number(X) > Number (X+ 1) Then
#            Temp <- Number(X)
#            Number (X) <- Number (X+ 1)
#            Number(X+I) <- Temp
#            Flag <- True
#        End If
#        X <- X+1
#    Until EndofArray
# Until Flag = False
#
########################################################
#

def getBiggerPoint(myList, i, j):
    if myList[i] >= myList[j]:
        return i
    else: 
        return j

def bubbleSort(myList):
    COUNT = 0
    counter = 1
    while counter < len(myList):
        position = 0
        i = 1
        while i <= len(myList) - counter:
            COUNT += 1
            position = getBiggerPoint(myList, position, i)
	    i += 1
        tmp = myList[len(myList) - counter]
        myList[len(myList) - counter] = myList[position]
        myList[position] = tmp
        counter += 1
        print(myList)
    print("count = %d" % COUNT)
    return myList

myList = [6,3,5,7,6,8,2,9]
print(myList)
bubbleSort(myList)
