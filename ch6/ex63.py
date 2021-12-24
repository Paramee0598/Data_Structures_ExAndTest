
def Power(i,p):
    if int(p) == 0 :
        return int(1)
    if int(p) == 1 :
        return int(i)
    if int(p) == 2 :
        return int(i)*int(i)
    if int(p) >=3 :
        return int(i) * (Power(i,p-1))

inp , pow = (input("Enter Input a b : ").split(" ")) ;inp = int(inp) ; pow = int(pow)
print(Power(inp,pow))



