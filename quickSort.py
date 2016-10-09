#!/usr/bin/python

#
################################################################
# divide and conquer
# pivot value/split point
# leftmark rightmark
# average time complexity: O(nlg(n))
# worst time complexity: O(n^2)
################################################################
#

def partition(myList, start, end):
    print(myList[start:end+1])
    # need some condition to end the recursion
    if start < end:
        pivot = quickSort(myList, start, end)
        print(myList[start:end+1])
        print(myList[start:pivot])
        print(myList[pivot+1:end+1])
        partition(myList, start, pivot - 1)
        partition(myList, pivot + 1, end)

def quickSort(myList, start, end):
# use the leftmost one as the pivot value
    pivot = myList[start]
    left = start + 1
    right = end
    count = 1
    while left <= right:
        # the order of the two conditions matter, if switched, it may lead to a index error
        while left <= end and myList[left] <= pivot:
            left += 1
        while right > start and myList[right] >= pivot:
            right -= 1
        if left < right:
            tmp = myList[left]
            myList[left] = myList[right]
            myList[right] = tmp
        count += 1

    tmp = myList[right]
    myList[right] = pivot
    myList[start] = tmp
    return right
myList = [5,6,3,7,4,8,2,7,9,6]
#myList=[6,3,5,4,8]
partition(myList, 0, len(myList) - 1)
print(myList)
