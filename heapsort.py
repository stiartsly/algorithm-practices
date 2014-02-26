import sys

def _maxHeapify(a, i, heapSize, cmpFunc):
    left  = 2*i
    right = left + 1
    largest = i
    if left  < heapSize and cmpFunc(a[largest], a[left]):
        largest = left
    if right < heapSize and cmpFunc(a[largest], a[right]):
        largest = right
         
    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        _maxHeapify(a, largest, heapSize, cmpFunc)
    
def _buildMaxHeap(a, heapSize, cmpFunc):
    for i in range(heapSize/2-1, -1, -1):
        _maxHeapify(a, i, heapSize, cmpFunc)


def heapSort(a, cmpFunc):
    heapSize = len(a)
    _buildMaxHeap(a, heapSize, cmpFunc)
    
    for i in range(heapSize-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapSize -= 1
        _maxHeapify(a,0, heapSize, cmpFunc)


#----------------------------
if __name__ == "__main__":
    def lessThan(a, b):
        return a <= b

    a = [5, 28, 3, 56, 23, 10, 35, 0, 9, 20, 1, 4,78, 892, -8]
    print "orignal array:\n", a
    
    heapSort(a, lessThan)
    print "array sorted with increasing order:\n", a

    def largerThan(a, b):
        return a > b
    heapSort(a, largerThan)
    print "arrary sorted with decreasing order:\n", a
    

    
