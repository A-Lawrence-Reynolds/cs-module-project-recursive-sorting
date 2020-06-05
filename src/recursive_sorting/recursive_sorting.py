# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    pointer_a = 0
    pointer_b = 0

    for x in range(elements):
        if pointer_a >= len(arrA):
            merged_arr[x] = arrB[pointer_b]
            pointer_b += 1
        elif pointer_b >= len(arrB):
            merged_arr[x] = arrA[pointer_a]
            pointer_a += 1
        elif arrA[pointer_a] > arrB[pointer_b]:
            merged_arr[x] = arrB[pointer_b]
            pointer_b += 1
        elif arrB[pointer_b] > arrA[pointer_a]:
            merged_arr[x] = arrA[pointer_a]
            pointer_a += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = arr[0:mid]

    right = arr[mid:len(arr)]

    return merge(merge_sort(left), merge_sort(right))

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):

        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):

        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here
    pass
    return arr
