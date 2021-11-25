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
        listPos1, listPos2 = 0, 0
        resList = []

        while listPos1 < ss1 and listPos2 < ss2:
            numComparisons += 1
            if subList1[listPos1] < subList2[listPos2]:
                resList.append(subList1[listPos1])
                listPos1 += 1
            else:
                resList.append(subList2[listPos2])
                listPos2 += 1

        if listPos1 > listPos2:
            resList += subList2[listPos2:]
        elif listPos2 > listPos1:
            resList += subList1[listPos1:]

        return resList

    return tList
print(' *** Merge sort ***')
inp = input('Enter some numbers : ');print()
arr = list(map(int, inp.split()))
print(f'Sorted -> {showStr(MergeSort(arr))}')
print(f'Data comparison =  {numComparisons}')