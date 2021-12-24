def Max(i):
  if len(i) == 1:
    return i[0]
  else:
    return i[0] if int(i[0]) > int(Max(i[1:])) else Max(i[1:]) #เอาทุกตัวยกเว้นตัวที่ 0
inp = input("Enter Input : ").split(" ")
print(f'Max : {Max(inp)}')


