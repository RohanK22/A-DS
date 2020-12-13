# Bubble sort on a list

def bubbleSort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - 1, (i + 1) - 1, -1):
            if A[j] < A[j - 1]:
                A[j],A[j - 1] = A[j - 1], A[j]
    return A

# Test Case
print(bubbleSort([3,2,5,6,8,4,20,0]))