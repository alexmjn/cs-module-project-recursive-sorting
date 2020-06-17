# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    j, k = 0, 0

    for i in range(len(merged_arr)):
        if k > len(arrB) - 1:
            merged_arr[i] = arrA[j]
            j += 1
        elif j > len(arrA) - 1:
            merged_arr[i] = arrB[k]
            k += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        elif arrB[k] < arrA[j]:
            merged_arr[i] = arrB[k]
            k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    j, k = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    arr = merge(j, k)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
