def weirdSubtract(n, k):
    c = lambda list: int("".join(map(str, list)))
    n = list(str(n))
    while (k != 0):
        if n[-1] == '0':
            del n[-1]
            k = k-1
        else:
            n = c(n)
            n=n-1
            k = k - 1
            if k > n :
                print("0")
                exit()
            n = list(str(n))
        if k== 0:break
    if k==0:
        n = c(n)
        print(n)
n, s = input("Enter num and sub : ").split()
weirdSubtract(int(n), int(s))