def merge(arr1, arr2):
    final_arr = []
    arr1_index = 0
    arr2_index = 0
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    for _ in range(arr1_len + arr2_len):
        if arr1_index < arr1_len and arr2_index < arr2_len:
            if arr1[arr1_index] >= arr2[arr2_index]:
                final_arr.append(arr2[arr2_index])
                arr2_index += 1
            else:
                final_arr.append(arr1[arr1_index])
                arr1_index += 1
        elif arr1_index == arr1_len:
            final_arr.append(arr2[arr2_index])
            arr2_index += 1
        else:
            final_arr.append(arr1[arr1_index])
            arr1_index += 1
    return final_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        median = len(arr) // 2
        return merge(merge_sort(arr[:median]), merge_sort(arr[median:]))


random_array = [1, 6, 3, 7, 8, 3, 6, 5, 2, 5, 6, 7, 3, 6, 3, 63, 65, 5, 7, 7, 79, 7, 4, 232, 4, 0]
sorted_list = merge_sort(random_array)
print(len(random_array))
print(len(sorted_list))
print(sorted_list)
