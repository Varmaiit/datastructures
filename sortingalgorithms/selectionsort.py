### Selection sort algorithm sorts an array by repetedly finding the minumum element from unsorted array.
# Ref : https://www.geeksforgeeks.org/selection-sort/

import copy


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


def recursive_bubble_sort(listt): 
    for i, num in enumerate(listt):
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                # print("listt", listt)
                recursive_bubble_sort(listt)
        except IndexError: 
            pass
    return listt 


# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 


if __name__ == "__main__":
    _list = [3, 4, 1, 79, 6, 6, 9, 45, 78]
    print("array inititally", _list)
    z = selection_sort(copy.deepcopy(_list))
    print("slection sort", z)
    print("array inititally", _list)
    print("bubble sort", bubbleSort(copy.deepcopy(_list)))
    print("recursive bubble sort", recursive_bubble_sort(_list))

