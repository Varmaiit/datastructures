### Selection sort algorithm sorts an array by repetedly finding the minumum element from unsorted array.
# Ref : https://www.geeksforgeeks.org/selection-sort/



def selection_sort(a):

    _len = len(a)
    for i in range(_len):
        _min = a[i]
        _min_index = i
        for j in range(i+1, _len):
            if _min > a[j]:
                _min = a[j]
                _min_index = j
        a[i], a[_min_index] = a[_min_index], a[i]

    return a


def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [3, 4, 1, 79, 6, 6, 9, 45, 78]
    print("sorted array", selection_sort(arr), bubbleSort(arr))

