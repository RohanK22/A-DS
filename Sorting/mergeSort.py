# Merge Sort on a list
import math;
Infinity = 10000

# Merge funtion which merges the two sub-arrays A[p..q] and A[q+1..r]
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(Infinity)
    R.append(Infinity)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i =  i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

# Test Case
li = [3,2,5,6,8,4,20,0]
mergeSort(li, 0, len(li) - 1)
print(li)