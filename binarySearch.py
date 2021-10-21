def binarySearch(array, number, start, end):
    middle = start + (end - start) // 2
    try:
        if start >= end:
            return None
        elif array[middle] == number:
            return middle
        else:
            if number > array[middle]:
                return binarySearch(array, number, middle + 1, end)
            else:
                return binarySearch(array, number, start, middle - 1)
    except IndexError:
        return None


testArray = [1, 6, 3, 7, 9, 1, 4, 2, 6, 9, 5, 3]
testArray.sort()

print(testArray)
print(binarySearch(testArray, 0, 0, len(testArray)))
