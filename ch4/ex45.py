count_mir = 0;count_nor = 0;Boom = 0;boom_nor = 0;stack_m = [];stack_n = [];to_queue = [];fail_boo_m = 0;can_boo_m = 0
Nor, Mirr = input("Enter Input (Normal, Mirror) : ").split();print("NORMAL :")
temp = ""
Mirr = "".join(reversed(Mirr))
#Mirror
for i in Mirr:
    if (stack_m == []):stack_m.append(i) ; temp = i ; count_mir += 1
    else:
        stack_m.append(i)
        if (temp == i):count_mir += 1
        else:temp = i ; count_mir = 1
        if (count_mir == 3):
            stack_m.pop();stack_m.pop(); Boom += 1;count_mir = 0;to_queue.append(stack_m.pop())  # stack ค่าที่จะใช้ต่อส่งไป normal
            if (stack_m != [] and len(stack_m) > 1):
                if (stack_m[-1] == stack_m[-2]):count_mir = 2 ; temp = stack_m[-1]
                else: count_mir = 1; temp = stack_m[-1]
            if (len(stack_m) == 1): count_mir = 1; temp = stack_m[-1]
# Normal
for i in Nor:
    if (stack_n == []):stack_n.append(i); count_nor += 1; temp = i
    else:
        stack_n.append(i)
        if (temp == i):count_nor += 1
        else: temp = i;count_nor = 1

        if (count_nor == 3):
            count_nor = 0
            if (to_queue != []):
                tempMiror = to_queue.pop(0)
                if (i == tempMiror):stack_n.pop(); stack_n.pop();stack_n.pop();stack_n.append(tempMiror);fail_boo_m += 1
                else:stack_n.pop() ;stack_n.append(tempMiror);stack_n.append(i)

            else: stack_n.pop();stack_n.pop();stack_n.pop();can_boo_m += 1 # เอาออกหมด กรณี ไม่มี mirror เลย
            if (stack_n != [] and len(stack_n) > 1):
                if (stack_n[-1] == stack_n[-2]): count_nor = 2;temp = stack_n[-1]
                else:temp = stack_n[-1];count_nor = 1
            if (len(stack_n) == 1): count_nor = 1; temp = stack_n[-1]

if (len(stack_n) >= 1):print(f'{len(stack_n)}\n{("".join(reversed(stack_n)))}')
else:print(f'{len(stack_n)}\nEmpty')
print(f'{can_boo_m} Explosive(s) ! ! ! (NORMAL)')
if (fail_boo_m > 0):print("Failed Interrupted", fail_boo_m, "Bomb(s)")
print("------------MIRROR------------\n: RORRIM")
if (len(stack_m) >= 1):print(f'{(len(stack_m))}\n{("".join(reversed(stack_m)))}\n(RORRIM) ! ! ! (s)evisolpxE {Boom}')
else: print(f'{(len(stack_m))}\nytpmE\n{("".join(reversed(stack_m)))}(RORRIM) ! ! ! (s)evisolpxE {Boom}')

