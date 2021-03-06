# Finding the subarray with the maximum sum
# CLRS Ch 4

import math


def findMaxSubarray(A, low, high):
    print('findMaxSubarray(', A[low:high + 1], ",", low, ",", high, ")")
    if high == low:  # Base case
        return (low, high, A[low])
    else:
        mid = math.floor((low + high)/2)
        (leftLow, leftHigh, leftSum) = findMaxSubarray(A, low, mid)
        (rightLow, rightHigh, rightSum) = findMaxSubarray(A, mid + 1, high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(A, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)  # Returning a tuple
        elif rightSum >= leftSum and rightSum >= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)


def findMaxCrossingSubarray(A, low, mid, high):
    print('findMaxCrossingSubarray(',
          A[low:high + 1], ",", low, ",", mid, ",", high, ")")
    leftSum = -10000
    sum = 0
    maxLeft = maxRight = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = -10000
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return (maxLeft, maxRight, leftSum + rightSum)


Array = [-13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 10, -5, -22, 15, -4, 7]
print(findMaxSubarray(Array, 0, len(Array) - 1))
