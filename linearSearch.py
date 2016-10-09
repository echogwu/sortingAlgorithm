#!/usr/bin/python
#
##############################################
# position <- 0
# found <- False
# while position < len(List) and not found:
#     if List[position] = item:
#         found <- True
#     position <- position + 1
##############################################
#
def linearSearch(myItem, myList):
    position = 0
    found = False
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
            print("The item %s is in the list, the position is %d" % (myItem, position))
        position += 1
    return found

myList = ['banana', 'apple', 'orange', 'kiwi']
myItem = 'diwi'
isFound = linearSearch(myItem, myList)
if not isFound:
    print("%s is not in the listi, going to add it to the list" % myItem)
    myList.append(myItem)
    print(myList) 
