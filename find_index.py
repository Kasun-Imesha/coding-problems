# binary search
def binary_search(arr, ele):
    mid = len(arr) // 2

    if len(arr) == 1:
        if arr[0] == ele:
            return ele   
        else:
            return None 

    if arr[mid] == ele:
        return ele

    elif arr[mid] < ele:
        return binary_search(arr[mid+1:], ele)

    else:
        return binary_search(arr[:mid], ele)

def binary_search_index(arr, ele, low, high):
    if low > high:
        return None
        
    mid = (low + high) // 2

    if arr[mid] == ele:
        return mid

    elif arr[mid] < ele:
        low = mid + 1

    else:
        high = mid - 1

    return binary_search_index(arr, ele, low, high)

a = [2, 4, 5, 7, 8, 10]
b = [10, 8, 7, 5, 4, 2]
c = [8, 7, 2, 10, 5, 4]
d = [8, 7, 2, 10, 5, 4, 7]
e = [8, 7, 2, 10, 5, 4, 3]

# for x in [1, 2, 7, 9, 10]:
#     print(f"{x} --> available: {binary_search(a, x) is not None}")

# print("--" * 10)

# for x in [1, 2, 7, 9, 10]:
#     print(f"{x} --> index: {binary_search_index(a, x, 0, len(a) - 1)}")

# exit(0)

# bubble sort

def bubble_sort(arr):
    while True:
        swapped = False

        for i in range(len(arr) - 1):
        
            if arr[i] > arr[i + 1]:
                ######
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                #####
                # tmp = arr[i]
                # arr[i] = arr[i + 1]
                # arr[i + 1] = tmp
                #####
                # arr[i] = arr[i] + arr[i + 1]
                # arr[i + 1] = arr[i] - arr[i + 1]
                # arr[i] = arr[i] - arr[i + 1]

                swapped = True

        if not swapped:
            break

    return arr

# for arr in [a, b, c]:
#     print(f"bubble_sort result of {arr} --> {bubble_sort(arr)}")

# merge sort

def merge_1(arr1, arr2):
    i = 0
    j = 0
    k = 0
    l1 = len(arr1)
    l2 = len(arr2)
    arr = [None] * (l1 + l2)

    while i < l1 and j < l2:

        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1

        k += 1

    if i < l1:
        for ele in arr1[i:]:
            arr[k] = ele
            k += 1
    elif j < l2:
        for ele in arr2[j:]:
            arr[k] = ele
            k += 1

    return arr

def merge_sort_1(arr):

    if len(arr) == 1:
        # print(arr)
        return arr

    mid = len(arr) // 2

    l_arr = arr[: mid]
    r_arr = arr[mid:]

    # print(f"{l_arr} -- {r_arr}")

    arr1 = merge_sort_1(l_arr)
    arr2 = merge_sort_1(r_arr)

    return merge_1(arr1, arr2)

# d = c
# print(merge([4,6,9], [1, 2, 10]))
# print(f"original arr: {d}")
# print(merge_sort(d))
# for arr in [a, b, c, d, e]:
#     print(f"merge_sort result of {arr} --> {merge_sort_1(arr)}")

def merge(a1, a2):
    i = 0
    j = 0
    k = 0
    l1 = len(a1)
    l2 = len(a2)
    arr = [None] * (l1 + l2)

    while i < l1 and j < l2:
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i += 1
        else:
            arr[k] = a2[j]
            j += 1

        k += 1

    if i < l1:
        for ele in a1[i:]:
            arr[k] = ele
            k += 1
    elif j < l2:
        for ele in a2[j:]:
            arr[k] = ele
            k += 1

    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    return merge(arr1, arr2)

for arr in [a, b, c, d, e]:
    print(f"merge_sort result of {arr} --> {merge_sort(arr)}")