
def findSecondSmallestNUmber(array):
    smallest = array[0]
    secondSmallest = array[1]
    # what if the first item is the smallest?

    for number in array:
        if number < smallest:
            # replace the secondSmallest before the value of the smallest changed
            secondSmallest = smallest
            smallest = number
    return secondSmallest

def findSecondSmallestNumber2(array):
    smallest = None
    secondSmallest = None
    for number in array:
        if smallest == None:
            smallest = number
        else:
            if number < smallest:
                secondSmallest = smallest
                number = smallest
            elif number > smallest:
                if secondSmallest == None:
                    secondSmallest = number
                # else:
                #     if number < secondSmallest:
                #         secondSmallest = number

    if len(array) > 1:
        if secondSmallest == None:
            secondSmallest = smallest
    return secondSmallest

def findSecondSmallestNumber3(array):
    array = list(set(array))   #remove the duplicates
    array.sort()
    if(len(array) < 2):
        secondSmallest = array[0]
    else:
        secondSmallest = array[1]
    return secondSmallest

arrayOfNum1 = [1,2,3,4,5,6,7,8,9,10]
arrayOfNum2 = [2,1,3,4,5,6,7,8,9,10]

arrayOfNum3 = [2,2,3,4,5,6,7,8,9,10]
arrayOfNum4 = [2,2,2,2,2,2]
arrayOfNum5 = [2,2,100]

print findSecondSmallestNUmber(arrayOfNum1)
print findSecondSmallestNUmber(arrayOfNum2)

print findSecondSmallestNumber2(arrayOfNum3)
print findSecondSmallestNumber2(arrayOfNum4)
print findSecondSmallestNumber2(arrayOfNum5)

print findSecondSmallestNumber3(arrayOfNum5)
print findSecondSmallestNumber3(arrayOfNum4)
print findSecondSmallestNumber3(arrayOfNum3)