def bubbleSort(array):
    swap = True
    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True

random_array = [1,6,3,7,8,3,6,5,2,5,6,7,3,6,3,63,65,5,7,7,79,7,4,232,4]

bubbleSort(random_array)
print(random_array)