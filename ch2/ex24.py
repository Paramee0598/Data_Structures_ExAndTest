def findTriplets(arr, n):
    show = []
    if len(arr) <= 2:
        print("Array Input Length Must More Than 2")
        exit()
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k] == 0)and(arr[i] == 0)and(arr[j] == 0)and(arr[k] == 0):
                    puk = [arr[i], arr[j], arr[k]]
                    show.append(puk)
                    print(show)
                    exit()
                if (arr[i] + arr[j] + arr[k] == 0):
                    puk = [arr[i], arr[j], arr[k]]
                    show.append(puk)
                    found = True
    if (found == False):
        pass
    print(show)
# Driver code
inpunumlist = input("Enter Your List : ").split()
arr = list(map(int,inpunumlist))
n = len(arr)
findTriplets(arr, n)

