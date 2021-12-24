
#ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร
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
    def pop(self,i):      # // นำข้อมูลออกจาก stack
        return self.items.pop(i)
    def isEmpty(self):    # // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []
    def size(self):   # // ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)

def oddEven(listStack):
 return_List = Stack()
 if len(listStack) == 1:
     return listStack
     exit()

 for j in listStack:
     if int(j) %2 == 0:
         j = int(j) - 1
         if int(j) <= 0:
             j = 1
         elif return_List.items != [] and int(j) < int(return_List.items[-1]):
             return_List.push(str(j))
         else:
             while return_List.items != [] and int(j) >= int(return_List.items[-1]):
                 return_List.pop(0)
             return_List.push(str(j))
         listStack.pop(0)

     if int(j) % 2 != 0:
         j = int(j) + 2
         if return_List.items != [] and int(j) < int(return_List.items[-1]):
             return_List.push(str(j))
         else:
             while return_List.items != [] and int(j) >= int(return_List.items[-1]):
                 return_List.pop(0)
             return_List.push(str(j))
     listStack.pop(0)
 return  return_List.items

def inToTheWood(woodNum):
 s = Stack()
 check = 0
 for i in woodNum:
     if i == "S":
         s.items = oddEven(s.items)
     elif i != "B" and i != "S":
         if s.items !=[]:
             if int(i) < int(s.items[-1]):
                 s.push(i)
             else:
                 while s.items != [] and int(i) >= int(s.items[-1]):
                     s.pop(0)
                 s.push(i)
         else:
             s.push(i)
     else :
         print(s.size())
inp = input('Enter Input : ')
inp = re.sub("A","",inp)
inp = re.sub(" ","",inp)
inp = inp.split(",")
inToTheWood(inp)