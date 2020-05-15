from math import log10
from random import randint
import timeit

// Testing Function
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

def countSortRadix(array,base,pos):

    countArray = [0]*base
    outputArray = [0]*len(array)
    for i in range(len(array)):
        countArray[array[i] // (base**pos) % base] += 1
    for i in range (1,base):
        countArray[i] = countArray[i] + countArray[i-1]
    for i in range(len(array)-1,-1,-1):
        outputArray[countArray[(array[i] // base ** pos) % base] -1 ] = array[i]
        countArray[((array[i] // base ** pos) % base) % base] -= 1
    return outputArray

def radixSort(array,base):

    if len(array)==0:
        return []
    valMax = max(array)
    poss = 0
    while(valMax):
        valMax=valMax // base
        poss += 1
    for pos in range(poss):
        array = countSortRadix(array,base,pos)
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
array = aux = [ randint(1, NrMax) for x in range(NrArray) ]

arrayTest = array

OK = 1
while OK == 1:
    Sorting = input("The sorting method is: ")
    if Sorting == "Quicksort":
        start = timeit.default_timer()
        quickSort(array, 0, len(array) - 1)
        stop = timeit.default_timer()
        execution_time = stop - start
        print("Program Executed in %s" % execution_time)
        sortingTest(array, arrayTest)
        print(array)
        array = aux
        print("-----------------------------")

    elif Sorting == "Bubble Sort":
        if len(array) > 3000:
            print("The sorting would take too long with this method")
            print("-----------------------------")
        else:
            start = timeit.default_timer()
            print(bubbleSort(array))
            stop = timeit.default_timer()
            execution_time = stop - start
            print("Program Executed in %s" % execution_time)
            sortingTest(array, arrayTest)
            array = aux
            print("-----------------------------")

    elif Sorting == "Count Sort":
        if max(array) > 1000000:
            print("The sorting would take too long with this method")
            print("-----------------------------")
        else:
            start = timeit.default_timer()
            countSort(array, max(array))
            stop = timeit.default_timer()
            print(array)
            execution_time = stop - start
            print("Program Executed in %s" % execution_time)
            sortingTest(array, arrayTest)
            array = aux
            print("-----------------------------")

    elif Sorting == "Radix Sort":
        start = timeit.default_timer()
        base = int(input("Specify the base: "))
        print(radixSort(array, base))
        stop = timeit.default_timer()
        execution_time = stop - start
        print("Program Executed in %s" % execution_time)
        sortingTest(array, arrayTest)
        array = aux
        print("-----------------------------")

    elif Sorting == "Merge Sort":
        start = timeit.default_timer()
        mergeSort(array)
        stop = timeit.default_timer()
        print(array)
        execution_time = stop - start
        print("Program Executed in %s" % execution_time)
        sortingTest(array, arrayTest)
        array = aux
        print("-----------------------------")

    elif Sorting == "Exit":
        OK = 0

