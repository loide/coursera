"""
Download the following text file:
    QuickSort.txt

The file contains all of the integers between 1 and 10,000 (inclusive, with no 
repeats) in unsorted order. The integer in the i_th row of the file gives you 
the i_th entry of an input array.

Your task is to compute the total number of comparisons used to sort the given 
input file by QuickSort. As you know, the number of comparisons depends on 
which elements are chosen as pivots, so we'll ask you to explore three different
 pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive 
call on a subarray of length m, you should simply add m-1 to your running total 
of comparisons. (This is because the pivot element is compared to each of the 
other m-1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, 
and different implementations can give you differing numbers of comparisons. For
 this problem, you should implement the Partition subroutine exactly as it is 
described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:

For the first part of the programming assignment, you should always use the 
first element of the array as the pivot element.

HOW TO GIVE US YOUR ANSWER:

Type the numeric answer in the space provided.

So if your answer is 1198233847, then just type 1198233847 in the space provided
without any space / commas / other punctuation marks. You have 5 attempts to get
 the correct answer.

(We do not require you to submit your code, so feel free to use the programming 
language of your choice, just type the numeric answer in the following space.)

"""
def partition_array(arr, start, end):
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
