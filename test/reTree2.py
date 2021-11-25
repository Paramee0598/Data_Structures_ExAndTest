def Min(i):
  if len(i) == 1:
    return i[0]
  else:
    return i[0] if int(i[0]) < int(Min(i[1:])) else Min(i[1:]) #เอาทุกตัวยกเว้นตัวที่ 0
inp = input("Enter Input : ").split(" ")
print(f'Min : {Min(inp)}')

