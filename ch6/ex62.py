showStr = lambda list : ''.join(map(str, list))
def Palindrome(str):
    if len(str) < 2: return print(f'\'{showStr(inp)}\' is palindrome')
    if str[0] != str[-1]: return print(f'\'{showStr(inp)}\' is not palindrome')
    return Palindrome(str[1:-1]) #หายตัวแรกไปทีละตัว
inp = [k for k in input("Enter Input : ")]
Palindrome(inp)

