def insert_recur(data,n):
    if(n <= 1):
        return
    insert_recur(data,n-1)
    templast = data[n-1]
    bfl = n-2
    bfl = forLoopRecursion(data,bfl,templast)
    data[bfl+1] = templast

    if(len(data) != n):
        print(f'insert {templast} at index {bfl+1} :', data[:n], data[n:])
    else:
        print(f'insert {templast} at index {bfl+1} :', data)
def forLoopRecursion(data, n, last):
    if(n < 0 or data[n] < last):   
        return n
    data[n+1] = data[n]   
    return forLoopRecursion(data, n-1, last) 


inp=[int(i) for i in input("Enter Input : ").split()]
total=insert_recur(inp,len(inp))
print("sorted\n"+str(inp))