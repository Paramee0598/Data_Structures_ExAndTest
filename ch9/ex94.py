showStr = lambda list : ''.join(map(str, list))
def sortRun(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        for j in range(i, -1, -1):
            if value < lst[j-1] and j > 0:
                lst[j] = lst[j-1]
            else:
                lst[j] = value
                break
    return lst


def get_median(sortedListed):
    length = len(sortedListed)
    if length % 2 == 0:
        return (sortedListed[length // 2 - 1] + sortedListed[length // 2]) / 2
    else:
        return sortedListed[length // 2]

def REre(x):
  return x[::-1]

if __name__ == '__main__':
    lst = list(map(int, input("Enter Input : ").split()))
    sorting = []
    set = []
    for item in lst:
        sorting.append(item)
        set.append(item)
        sortRun(sorting)
        #sortingStr = showStr(str(sorting))

        print(f"list = {set} : median = {get_median(sorting):.1f}")