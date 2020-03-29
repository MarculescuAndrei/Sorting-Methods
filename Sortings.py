from random import randint

Sorting = input("The sorting method is: ")

import timeit

def sortingTest(array1, array2):
    array2.sort()
    if array1 == array2 :
        print("The sorting is correct")
    else:
        print("The sorting is not correct")

#______________QuickSort______________#

def partition(array, start, end):

    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def quickSort(array, start, end):

    if start >= end:
        return
    p = partition(array, start, end)
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)

#______________BubbleSort______________#

def bubbleSort(array):

        for i in range(len(array)):
            for j in range(len(array) - 1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array
#______________CountSort______________#

def countSort(array, max):

        m = max + 1
        count = [0] * m

        for a in array:
            count[a] += 1
        i = 0
        for a in range(m):
            for c in range(count[a]):
                array[i] = a
                i += 1
        return array

#______________RadixSort______________#

def countSortDigits(array, cif):
    out = [0] * len(array)
    fq = [0] * 10
    for i in range(len(array)):
        ind = array[i] // cif
        fq[ind % 10] = fq[ind % 10] + 1
    for i in range(1, 10):
        fq[i] += fq[i - 1]

    i = len(array) - 1
    while i >= 0:
        ind = array[i] // cif
        out[fq[ind % 10] - 1] = array[i]
        fq[ind % 10] = fq[ind % 10] - 1
        i = i - 1

    for i in range(0, len(array)):
        array[i] = out[i]


def radixSort(array):
    m = max(array)
    cif = 1
    while m / cif > 0:
        countSortDigits(array, cif)
        cif = cif * 10
    return array

#______________MergeSort______________#

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

# ______________Main______________#


NrMax = int(input("The biggest number from the array is: "))
NrArray = int(input("The number of elements in the array is: "))
array = l = [ randint(1, NrMax) for x in range(NrArray) ]

arrayTest = array
start = timeit.default_timer()

if Sorting == "Quicksort":
    quickSort(array, 0, len(array) - 1)
    print(array)

elif Sorting == "Bubble Sort":
    if len(array) > 3000:
        print("The sorting would take too long with this method")
    else:
        print(bubbleSort(array))

elif Sorting == "Count Sort":
    if max(array) > 1000000:
        print("The sorting would take too long with this method")
    else:
        countSort(array, max(array))
        print(array)

elif Sorting == "Radix Sort":
    print(radixSort(array))

elif Sorting == "Merge Sort":
    mergeSort(array)
    print(array)


stop = timeit.default_timer()
execution_time = stop - start

sortingTest(array, arrayTest)
print("Program Executed in %s" % execution_time)
