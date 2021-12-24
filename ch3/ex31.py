class Stack:
    def __init__(self, q = None): #// ใช้สำหรับสร้าง list ว่าง
        if q == None:
            self.items = []
        else:
            self.items = q
    def push(self, i):      #// เก็บข้อมูลลง stack
        self.items.append(i)
    def pop(self):      # // นำข้อมูลออกจาก stack
        return self.items.pop(0)
    def isEmpty(self):    # // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []
    def size(self):   # // ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)
print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter i to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(),"Data in stack : ",s.items)
while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s.items)