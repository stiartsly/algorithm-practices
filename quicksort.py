import sys
import random

def quickSort(a, low, high, cmpFunc):
    if low >= high:
        return 
    rand = random.randint(low, high)
    if rand != high:
        a[rand], a[high] = a[high], a[rand]    

    i = low - 1
    pivot = a[high]

    for j in range(low, high):
        if cmpFunc(a[j], pivot):
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[high] = pivot, a[i]

    if (low < i-1):
        quickSort(a, low, i-1, cmpFunc)
    if (i+1 < high):
        quickSort(a, i+1, high, cmpFunc)

def quickSortNoRecursion(a, low, high, cmpFunc):
    pass

if __name__ == "__main__":
    a = [3, 44, 544, 5, 40, 50, 60, 80, 1, 0, 90, 35, 33,89, 190, 888]

    def lessThan(a, b):
        return a < b 
    print "original array: \n", a
    quickSort(a, 0, len(a) -1, lessThan)
    print "array sorted with decreasing order:\n", a

    a = [3, 44, 544, 5, 40, 50, 60, 80, 1, 0, 90, 35, 33,89, 190, 888]
    def largerThan(a, b):
        return a > b
    quickSort(a, 0, len(a) -1, largerThan)
    print "array sorted with increasing order:\n", a

