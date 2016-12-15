#!/usr/bin/python

###########################################################
# 
##########################################################

def partition(myList):
    leng = len(myList)
    increment = leng/2
    while increment > 0:
        start = 0
        while start < increment:
            print("start = %d, increment = %d" % (start, increment))
            shellSort(myList, start, increment) 
            start += 1 
        increment /= 2
    return myList

def shellSort(myList, start, increment):
    leng = len(myList)
    for i in range(start + increment, leng, increment):
        currentValue = myList[i]
        j = i - increment
        while j >= start:
            if myList[j] > currentValue:
                myList[j + increment] = myList[j]
                j -= increment
            else:
                myList[j + increment] = currentValue
                break
        if j < start:
            myList[start] = currentValue
    print(myList)
    return myList

myList = [3,2,6,1,5]
print("original list is:\n%s\n===========" % myList)
partition(myList)
