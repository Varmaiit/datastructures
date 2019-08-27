# Sort a binary array in O(n)
# Ref: https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/



# A Python program to sort a Terenary array
def sortTerenaryArray(a):
    lo = 0
    mid = 0 
    hi = len(a) -1
    while mid <= hi:
        print("aaaaa before", a, lo, mid, hi)
        if a[mid] == 0:
            print("oooo", a[lo], a[mid])
            a[lo], a[mid] = a[mid], a[lo]
            lo += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi -= 1
        print("aaaaa after", a, lo, mid, hi)
        print("\n")
    return a     


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

print("final array", sortTerenaryArray(arr))


    