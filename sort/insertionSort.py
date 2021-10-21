def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert


random_array = [1, 6, 3, 7, 8, 3, 6, 5, 2, 5, 6, 7, 3, 6, 3, 63, 65, 5, 7, 7, 79, 7, 4, 232, 4, 0]

insertion_sort(random_array)
print(random_array)
