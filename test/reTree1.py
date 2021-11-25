def natural_sum(n):
    if(n!=1):
        sumNum = n + natural_sum(n-1)
        print(" +",n,end="")
        return sumNum
    print("1", end="")
    return  1
print(" *** Natural sum ***")
num = int(input("Enter number : "))
print(" =","%.d" %(natural_sum(num)))