def merge(arr1, arr2):
    if not len(arr1) or not len(arr2):
        return arr1 or arr2

    arr_result = []
    i,j = 0, 0

    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] <= arr2[j]:
            arr_result.append(arr1[i])
            i+=1
        else:
            arr_result.append(arr2[j])
            j+=1

        if (i == len(arr1) or j == len(arr2)):
            arr_result.extend(arr1[i:] or arr2[j:])

    return arr_result

def merge_sort(arr):
    if (len(arr) < 2):
        return arr

    middle = len(arr)/2
    arr1 = arr[:int(middle)]
    arr2 = arr[int(middle):]

    arr1 = merge_sort(arr[:int(middle)])
    arr2 = merge_sort(arr[int(middle):])
    return merge(arr1,arr2)

def loadData(arr):
    """Load data from input file """
    f = open("IntegerArray.txt","r")
    for line in f:
        arr.append(int(line))

    f.close()

def main():
    arr = []
    loadData(arr)

    arr = merge_sort(arr)
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()
