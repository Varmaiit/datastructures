### Count 1's in a sorted binary array
# Ref : https://www.geeksforgeeks.org/count-1s-sorted-binary-array/



arr = arr=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def countOnes(arr, lo, hi):
    count = 0
    count +=1
    print(count)
    # if high is equal or greater than lo it mean no 1's exist in the sorted binary array
    if hi>=lo:

        mid = lo + (hi-lo)//2
        # print(mid,"type", type(mid))

        if (arr[mid] == 1):
            if (arr[mid+1] == 0) or (mid==hi):
                return mid+1
            return countOnes(arr, mid+1, hi)

        return countOnes(arr, lo, mid -1)

    return 0


if __name__ == "__main__":
    print("Number of 1's", countOnes(arr, int(0), int(len(arr)-1)))


