# Insertion Sort on a List 
def insertionSort(l):
  for j in range(1, len(l)): 
    # Note: range(start, end) does not include the end  
    key = l[j]
    i = j - 1
    while i >= 0 and l[i] > key:
      l[i + 1] = l[i]
      i = i - 1
    l[i+1] = key
  return l

# Test Case
print(insertionSort([3,2,5,6,8,4,20,0]))