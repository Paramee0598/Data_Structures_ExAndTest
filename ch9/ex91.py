arr = list(map(int, input("Enter Input : ").split()))

def bubbleSort(array):
    count = 0
    for idx in range(len(array)-1):
        if array[idx] > array[idx + 1]:
            array[idx],array[idx + 1] = array[idx + 1],array[idx]
            count += 1

    if count == 0:
        return array
    else:
        return bubbleSort(array)

print(bubbleSort(arr))