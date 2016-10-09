#!/usr/bin/python

#
#####################################################################
# Procedure InsertionSort (List, First, Last)
#     For CurrentPointer <- First + 1 To Last
#         CurrentValue <- List[CurrentPointer]
#         Pointer <- CurrentPointer - 1
#         While List[Pointer] > CurrentValue AND Pointer > 0
#             List[Pointer+1] <- List[Pointer]
#             Pointer <- Pointer - 1
#         EndWhile
#         List[Pointer+1] <- CurrentValue
#     EndFor
# EndProcedure
#####################################################################
#

def insertionSort(myList):
    COUNT = 0
    print(myList)
    leng = len(myList)
    first = 1
    while first <= leng - 1:
        currentValue = myList[first]
        pointer = first - 1
        while pointer >= 0 and currentValue < myList[pointer]:
            COUNT += 1
            myList[pointer + 1] = myList[pointer]
            pointer -= 1 
        myList[pointer + 1] = currentValue
        print(myList)
        first += 1
    print(COUNT)
    return myList

myList = [6,3,5,7,6,8,2,9]
insertionSort(myList)
