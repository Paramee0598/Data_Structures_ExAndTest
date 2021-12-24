def staircase(n):
    print('Not Draw!') if n == 0 else 0
    def print_underscore(space):
        if (space == 0):
            return

        print("_", end="")

        print_underscore(space - 1)

    def print_sharp(sharp):
        # base case
        if (sharp == 0):
            return

        print("#", end="")

        print_sharp(sharp - 1)

    def pattern(n, num):
        # base case
        if (n == 0):
            return

        print_underscore(n - 1)
        print_sharp(num - n + 1)
        print()

        pattern(n - 1, num)

    def pattern_invert(n, num):
        # base case
        # base case
        if (n == 0):
            return
        print_underscore(num - n )
        print_sharp(n)


        print()

        pattern_invert(n - 1, num)


    if n > 0:
        pattern(n, n)
    if n < 0:
        n = n*(-1)
        pattern_invert(n,n)

staircase(int(input("Enter Input : ")))