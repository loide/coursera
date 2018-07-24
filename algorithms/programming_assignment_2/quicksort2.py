"""
See the first question.

DIRECTIONS FOR THIS PROBLEM:

Compute the number of comparisons (as in Problem 1), always using the final 
element of the given array as the pivot element. Again, be sure to implement 
the Partition subroutine exactly as it is described in the video lectures.

Recall from the lectures that, just before the main Partition subroutine, you 
should exchange the pivot element (i.e., the last element) with the first element.

***Note: This exercises uses the last element as the pivot but to do it, first
switches the last element to the first position and then the partition ensues.
This is how this algorithm is given in popular algorithm texts.
"""
def partition_array(arr, start, end):
    #swipe first and last element
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp

    pivot = arr[start]
    i = start + 1
    j = start + 1
    comparisons = end - start
    while (j <= end):
        if (arr[j] < pivot):
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            i+=1
        j+=1
    # swap arr[start] and arr[i-1]
    arr[start] = arr[i-1]
    arr[i-1] = pivot
    return i-1, comparisons

def sort(arr):
    if (len(arr) == 1):
        return
    else:
        return quicksort(arr, 0, len(arr) - 1)

def quicksort(arr, start, end):
    n_comparisons = 0
    if (start < end):
        pivot_point, n_comparisons = partition_array(arr, start, end)
        n_comparisons += quicksort(arr, start, pivot_point - 1)
        n_comparisons += quicksort(arr, pivot_point + 1, end)
    return n_comparisons

def loadData(arr):
    """Load data from input file """
    f = open("QuickSort.txt","r")
    for line in f:
        arr.append(int(line))

    f.close()

def main():
    arr = []
    loadData(arr)

    #"""Print unsorted array """
    #print (arr)
    c = sort(arr)
    print (c)
    #""""Print sorted array"""
    #print(arr)

if __name__ == "__main__":
    main()
