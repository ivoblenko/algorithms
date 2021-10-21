def selectionSort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


random_array = [1, 6, 3, 7, 8, 3, 6, 5, 2, 5, 6, 7, 3, 6, 3, 63, 65, 5, 7, 7, 79, 7, 4, 232, 4, 0]

selectionSort(random_array)
print(random_array)
