showStr = lambda list : ''.join(map(str, list))
listBan = ['?','“','”',';','’','!','.',' ' ]
def Palindrome(str):
    if len(str) < 2: return print(f'\'{inpPre}\' is palindrome')
    if str[0] != str[-1]: return print(f'\'{showStr(inpPre)}\' is not palindrome')
    return Palindrome(str[1:-1]) #หายตัวแรกไปทีละตัว
inpPre = input("Enter Input : ")
inp = []
for k in inpPre :
    if k not in listBan: inp.append(k.lower())
Palindrome(inp)
