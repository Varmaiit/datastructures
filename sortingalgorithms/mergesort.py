### Selection sort algorithm sorts an array by repetedly finding the minumum element from unsorted array.
# Ref : https://www.geeksforgeeks.org/selection-sort/

import copy


def merge_two_sorted_arrays(arr1, arr2):
    """ Merging of two sorted arrays is the core of the algorithm for merge sort"""
    _len1 = len(arr1)
    _len2 = len(arr2)
    arr3 = [None] * (_len1 + _len2)

    i, j, k = 0, 0, 0

    while i < _len1 and j < _len2:

        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr3[k] = arr2[j]
            j += 1
            k += 1

    
        
    while i < _len1:
        arr3[k] = arr1[i]
        k += 1
        i += 1

    while j < _len2:
        arr3[k] = arr2[j]
        k  += 1 
        j  += 1
    return arr3




if __name__ == "__main__":
    _list1 = [1, 3, 7, 11, 15, 17, 20, 21, 30, 35]
    _list2 = [2, 4, 5, 6, 12, 23, 45]
    new_list =merge_two_sorted_arrays(_list1, _list2)
    print("arrayyy", new_list)



