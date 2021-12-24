def maxIndex(lis, index=0):
    if index == len(lis)-1:
        return index
    k = maxIndex(lis,index+1)
    maxIndex(lis,index+1)
    return index if lis[index] > lis[k] else k
def sort(lis, stop):
    if stop == 0:
        return
    nowLis=lis.copy()
    mxIndex = maxIndex(nowLis[:stop+1])
    mx=lis[mxIndex]
    if mxIndex != stop:
        temp=lis[stop]
        lis[mxIndex]=lis[stop]
        lis[stop]=mx
        print('swap {0} <-> {1} : '.format(temp,mx) + str(lis))
    sort(lis,stop-1)

inp=[int(e) for e in input('Enter Input : ').split()]
temp = inp.copy()
sort(temp,len(temp)-1)
print(temp)