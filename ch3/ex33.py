showStr = lambda list : ''.join(map(str, list))
class Stack:
    def __init__(self, q = None): #// ใช้สำหรับสร้าง list ว่าง
        if q == None:
            self.items = []
        else:
            self.items = q
    def push(self, i):      #// เก็บข้อมูลลง stack
        self.items.append(i)
    def pop(self):      # // นำข้อมูลออกจาก stack
        return self.items.pop()
    def pop(self,i):  # // นำข้อมูลออกจาก stack
        return self.items.pop(i)
    def isEmpty(self):    # // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []
    def size(self):   # // ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)

def coloeCrush(Az):
    s = Stack()
    check = False
    checkTime = 0
    checkTime_1 = 0
    for c in Az:
       s.push(c)
    if s.size() <= 2 :
        s.items.reverse()
        print(s.size())
        print(showStr(s.items))
        exit()
    while check == False:
     for i in range(0, len(s.items)-2):
        for j in range(i + 1, len(s.items) - 1):
            for k in range(j + 1, len(s.items)):
                #print(f'{s.items[i]}{s.items[j]}{s.items[k]}')
                if s.items[i] == s.items[j] == s.items[k]:
                    s.items.pop(i)
                    s.items.pop(j-1)
                    s.items.pop(k-2)
                    checkTime += 1
                    check = True
                    break
     if s.size() >= 3 and checkTime != 3 :
         check = False
         checkTime_1 +=1
     if s.size() >= 3 and checkTime == 3 and check == False:
         check = True
     if s.size() >= 3 and checkTime_1 >= 3 and check == False:
         break
    show = s.items
    show.reverse()
    print(f'{len(show)}')
    if not s.isEmpty():print(f'{showStr(show)}')
    if s.isEmpty() : print('Empty')
    if checkTime >= 2 :
        print(f'Combo : {checkTime} ! ! !')
inp = input('Enter Input : ').split()
coloeCrush(inp)