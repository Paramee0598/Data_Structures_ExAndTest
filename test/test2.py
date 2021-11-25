showStr = lambda list : ' '.join(map(str, list))
def cal(input):
 if input == 0 :
     print('0 is OUT of range !!!')
     exit()
 show = []
 for i in range(1,input+1):
     if  int(input) % int(i) == 0:
         show.append(i)
 print(f'Output ==> {showStr(show)}')
 print(f'Total ==> {len(show)}')

print(' *** Divisible number ***')
inp = input("Enter a positive number : ")
cal(int(inp))


