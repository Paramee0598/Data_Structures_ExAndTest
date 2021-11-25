showStr = lambda list : ' '.join(map(str, list))


def Rere1(input):
    onechr = input[-1]
    reStr =  input[0:-1:]
    reStr =   onechr + reStr
    return reStr

def Rere2(input):
    onechr = input[0]
    reStr =  input[1::]
    reStr =   reStr + onechr
    return reStr

print('*** String Rotation ***')
str1 , str2 = input("Enter 2 strings : ").split(" ")

check1 = str1
check2 = str2

show1 = Rere1(str1)
show2 = Rere2(str2)
show1real = Rere1(str1)
show2real = Rere2(str2)
print(f'1 {show1} {show2}')
i = 2
OUT = False

while OUT != True:
    if (str(show1real) != str(check1) ) or (str(show2real) != str(check2)):
     inp1 = show1
     inp2 = show2
     show1real = Rere1(inp1)
     show2real = Rere2(inp2)
     show1 = show1real
     show2 = show2real
     if i <= 5 :
      print(f'{i} {show1real} {show2real}')

     i = i + 1

    else:
        if i ==7 :
          print(f'{i-1} {show1real} {show2real}')
          print(f'Total of  {i-1} rounds.')
          break

        if i > 5  :
            print(' . . . . . ')
            print(f'{i-1} {show1real} {show2real}')
        print(f'Total of  {i-1} rounds.')
        break

    if i > 6:
        pass












