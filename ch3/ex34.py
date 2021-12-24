import re
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
    def isEmpty(self):    # // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []
    def size(self):   # // ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)
def inToTheWood(woodNum):
 s = Stack()
 for i in woodNum:
     if i != "B":
         if s.items !=[]:
             if int(i) < int(s.items[-1]):
                 s.push(i)
             else:
                 while s.items != [] and int(i) >= int(s.items[-1]):
                     s.pop()
                 s.push(i)
         else:
             s.push(i)
     else :
         print(s.size())
         print(s.items)
inp = input('Enter Input : ')
inp = re.sub("A","",inp)
inp = re.sub(" ","",inp)
inp = inp.split(",")
inToTheWood(inp)