numComparisons = 0
showStr = lambda list : ' '.join(map(str, list))

def MergeSort(tList):
    global numComparisons

    lsz = len(tList)
    if lsz > 1:
        midPoint = lsz // 2

        subList1 = MergeSort(tList[:midPoint])
        subList2 = MergeSort(tList[midPoint:])

        ss1, ss2 = len(subList1), len(subList2)
        i1, i2 = 0, 0
        resList = []

        while i1 < ss1 and i2 < ss2:
            numComparisons += 1
            if subList1[i1] < subList2[i2]:
                resList.append(subList1[i1])
                i1 += 1
            else:
                resList.append(subList2[i2])
                i2 += 1

        if i1 > i2:
            resList += subList2[i2:]
        elif i2 > i1:
            resList += subList1[i1:]

        return resList

    return tList
inp = input('Enter some numbers : ');print()
arr = list(map(int, inp.split()))
print(f'Sorted -> {showStr(MergeSort(arr))}')
print(f'Data comparison =  {numComparisons}')