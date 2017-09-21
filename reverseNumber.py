# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
# Example1: x = 123, return 321
# Example2: x = -123, return -321


# 32 bits signed max: 2^31 -1 = 2xxx xxx xxx

def reverseNum(number):

    max32BitSignedInt = 2**31-1
    max32BitSignedNegInt = -2**31

    # max32BitSignedIntStr = str(max32BitSignedInt)
    # max32BitSignedIntStrReversed = max32BitSignedIntStr[::-1]
    # max32BitSignedIntReversed = int(max32BitSignedIntStrReversed)

    if number < 0:
        number = -number
        numStr = str(number)
        numStr = numStr[::-1]
        number = int(numStr)
        number = -number
        if number < max32BitSignedNegInt:
            return 0
    else:
        numStr = str(number)
        numStr = numStr[::-1]
        number = int(numStr)
        if number > max32BitSignedInt:
            return 0

    return number


print reverseNum(123)
print reverseNum(-123)
print reverseNum(2147483642)
print reverseNum(654321)
print reverseNum(-654321)



def intToBinary(num):
    return '{0:032b}'.format(num)