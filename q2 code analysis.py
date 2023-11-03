
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False


def findPairsWithSum(arr, target):
    arr = mergeSort(arr)
    for i in arr:
        if binarySearch(arr, target - i):
            print(f"Pair found: ({i}, {target - i})")
            
S = [1, 3, 5, 7, 8, 9]
target = 10
findPairsWithSum(S, target)

import time
import random
import matplotlib.pyplot as plt

def measureRunningTime(n):
    S = [random.randint(1, 100) for _ in range(n)]
    target = random.randint(1, 200)
    
    startTime = time.time()
    findPairsWithSum(S, target)
    endTime = time.time()
    
    return endTime - startTime

nValues = list(range(1, 1000)) + [10, 100, 1000, 10000, 100000, 1000000]
times = []

for n in nValues:
    timeTaken = measureRunningTime(n)
    times.append(timeTaken)

plt.plot(nValues, times,marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Merge Sort and Binary Search using Divide-Conquer')
plt.show()



