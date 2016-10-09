#!/usr/bin/python

#
#######################################################
# counter <- 1
# Repeat
#    position <- 0
#    X <- StartofArray
#    Repeat
#        if Number(X) >= Number(position) Then
#            position = X
#        End If
#        X <- X+1
#    Until EndofArray
#    tmp = Number(len(Array)-counter)
#    Number(len(Array)-counter)=Number(position)
#    Number(position)=tmp
#    counter <- counter+1
# Until counter = len(Array) - 1
#
########################################################
#

def selectionSort(myList):
    COUNT = 0
    counter = 1
    while True:
        flag = False
        position = 0
        while position <= len(myList) - (1 + counter):
            COUNT += 1
            if myList[position] >= myList[position + 1]:
                flag = True
                tmp = myList[position]
                myList[position] = myList[position + 1]
                myList[position + 1] = tmp
            position += 1
            print(myList)
        counter += 1
        if not flag:
            break
    print("count = %d" % COUNT)
    return myList

myList = [6,3,5,7,6,8,2,9]
print(myList)
selectionSort(myList)


