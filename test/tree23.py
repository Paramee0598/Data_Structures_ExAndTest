

def insertionRecursion(array, n):
    # base case
    if n <= 1:
        return
    insertionRecursion(array, n-1)  # for bigger to small...

    last = array[n-1]   # store last value
    j = n - 2   # store before last index

    j = forLoopRecursion(array, j, last)     # for loop recursive

    array[j+1] = last   # assign last to the right position

    #if len(array) != n:
     #   print(f'insert {last} at index {j+1} :', array[:n], array[n:])

    #else:
     #   print(f'insert {last} at index {j+1} :', array)
     #   print(f' last = {last}')



def forLoopRecursion(array, j, last):
    # base case
    if j < 0 or array[j] < last:   # out of range and left is less than right

        return j


    array[j+1] = array[j]   # shift left position to right
    return forLoopRecursion(array, j-1, last)   # go left



def insertionSort(arr):
    # Traverse through 1 to len(arr)
    num = 1
    numShow = 0
    check = 0
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        #print(key)
      #  print('before', arr)
        while j >= 0 and key < arr[j]:

            arr[j + 1] = arr[j]
           # print('loop', arr,f'num = {num}')
            check =+1
            num +=1
            j -= 1
        arr[j + 1] = key
      #  print('after',arr)
        numShow +=1
    if num == 1:
        #print('1 = 1')
        print(f'Data comparison =  {numShow}')
        #print(f'Data comparison = num {num}')
    else:
        if num-1 == (len(arr)*3):
            print(f'Data comparison =  {(len(arr)*3)}')
            exit()
        #if check == True and num == 2:
        #   print(f'Data comparison =  {(len(arr) - 1)*2}')
         #   exit()
        if( check == 1 )&(num >= 2):
            print(f'Data comparison =  {(num+numShow)-2}')
           # print(f'num = {num}')
           # print(f'check = {check}')
           # print(f'show num{numShow}')
            exit()

       # print('else case')
        print(f'Data comparison =  {num-1}')
       # print(f'check = {check}')
      # print(f'show num{numShow}')


    # Driver code to test above
#len -1
print(' *** Insertion sort ***')
inp = input('Enter some numbers : ')
#arr = [2 ,3, 4, 5, 6, 7, 8, 9, 10 ,1]
arr  = list(map(int, inp.split()))

lst = [int(i) for i in inp.split()]

insertionRecursion(lst, len(lst))
print()
print(lst)
insertionSort(arr)

#for i in range(len(arr)):
    #print("% d" % arr[i])