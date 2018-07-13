"""
Download the following text file:
    IntegerArray.txt

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith
row of the file indicates the ith entry of an array.

Because of the large size of this array, you should implement the fast
divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided
without any space / commas / any other punctuation marks. You can make up to 5
attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming
language you want --- just type the final numeric answer in the following space
.)

[TIP: before submitting, first test the correctness of your program on some
small test files or your own devising. Then post your best test cases to the
discussion forums to help your fellow students!]
"""

def merge(arr1, arr2, inversions):
    if not len(arr1) or not len(arr2):
        return arr1,0 or arr2,0

    arr_result = []
    i,j = 0, 0

    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] <= arr2[j]:
            arr_result.append(arr1[i])
            i+=1
        else:
            arr_result.append(arr2[j])
            j+=1
            inversions+=(len(arr1) - i)

    if (i == len(arr1) or j == len(arr2)):
        arr_result.extend(arr1[i:] or arr2[j:])

    return arr_result, inversions

def merge_sort(arr):
    if (len(arr) < 2):
        return arr,0

    middle = len(arr)/2
    arr1 = arr[:int(middle)]
    arr2 = arr[int(middle):]

    arr1,arr1_inversions = merge_sort(arr[:int(middle)])
    arr2,arr2_inversions = merge_sort(arr[int(middle):])
    inversions = 0 + arr1_inversions + arr2_inversions
    return merge(arr1,arr2,inversions)

def loadData(arr):
    """Load data from input file """
    f = open("IntegerArray.txt","r")
    for line in f:
        arr.append(int(line))

    f.close()

def main():
    arr = []
    loadData(arr)

    arr,n_inversions = merge_sort(arr)

    """Print sorted array """
    #for i in arr:
    #    print(i)

    print("Total inversions: " + str(n_inversions))

if __name__ == "__main__":
    main()
