# 333333333333333333333333

input_bet = input("Enter number end with (-1) : ").split(' ')
check = False
if not '-1' in input_bet :
    print('Invalid INPUT !!!')
    exit()
cal = []
for i in input_bet:
    if i != '-1':
     cal.append(i)
    if i =='-1':
        break
lennn = int((len(cal))/2)
for j in cal:
    show = int(cal.count(j))
    if show >=lennn:
      print(j)
      check = True
      break
if check == False :
    print('Not found')




